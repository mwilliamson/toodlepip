import os
from datetime import timedelta

import tempman
import xdg.BaseDirectory

from . import config, files
from .consoles import Console


class PythonBuilder(object):
    def __init__(self, console):
        self._console = console

    def matrix(self, project_config):
        return project_config.get_list("python", ["2.7"])
    
    def create_runtime(self, path, entry):
        python_version = entry
        temp_dir = self._create_temp_dir()
        try:
            working_dir = temp_dir.path
            
            project_dir = os.path.join(working_dir, "project")
            virtualenv_dir = os.path.join(working_dir, "virtualenv")
            self._console.run_all(
                "Copying project",
                [],
                quiet=True,
            )
            files.copy(path, project_dir)
            self._create_virtualenv(virtualenv_dir, python_version)
        except Exception:
            temp_dir.close()
            raise
        return PythonRuntime(self._console, temp_dir, project_dir, virtualenv_dir)
    
    def _create_temp_dir(self):
        temp_root = tempman.root(
            xdg.BaseDirectory.save_data_path("toodlepip/tmp"),
            timeout=timedelta(days=1)
        )
        return temp_root.create_temp_dir()
    
    def _create_virtualenv(self, path, python_version):
        python_binary = self._python_binary(python_version)
        
        def _pip_upgrade(package_name):
            pip = os.path.join(path, "bin", "pip")
            return [pip, "install", "--upgrade", package_name]
        
        commands = [
            ["virtualenv", path, "--python={0}".format(python_binary)],
            _pip_upgrade("pip"),
            _pip_upgrade("setuptools"),
            _pip_upgrade("virtualenv"),
        ]
        
        self._console.run_all(
            "Creating virtualenv",
            commands,
            quiet=True,
        )
        
        
    def _python_binary(self, python_version):
        if python_version == "pypy":
            return "pypy"
        else:
            return "python{0}".format(python_version)


class PythonRuntime(object):
    def __init__(self, console, temp_dir, project_dir, virtualenv_dir):
        self._console = console
        self._temp_dir = temp_dir
        self._project_dir = project_dir
        self._virtualenv_dir = virtualenv_dir
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self._temp_dir.close()

    def run_step(self, step):
        virtualenv_activate = os.path.join(self._virtualenv_dir, "bin/activate")
        
        def _virtualenv_run_all(description, commands):
            commands = map(_virtualenv_command, commands)
            self._console.run_all(
                description,
                commands,
                cwd=self._project_dir
            )
        
        def _virtualenv_command(command):
            return [
                "sh", "-c",
                ". {0}; {1}".format(virtualenv_activate, command)
            ]
        
        _virtualenv_run_all("Running {0} commands".format(step.name), step.commands)


_default_builders = {
    "python": PythonBuilder
}

def create_builder(shell, stdout):
    return Builder(_default_builders, Console(shell, stdout))


class Builder(object):
    def __init__(self, builders, console):
        self._console = console
        self._builders = builders
    
    def build(self, path):
        project_config = config.read(path)
        
        language = project_config.language
        language_builder = self._builders[project_config.language](self._console)
        
        for entry in language_builder.matrix(project_config):
            self._build_entry(language_builder, path, project_config, entry)
            
    def _build_entry(self, language_builder, path, project_config, entry):
        with language_builder.create_runtime(path, entry) as runtime:
            for step in self._steps(project_config):
                runtime.run_step(step)
        
    def _steps(self, project_config):
        for name in ["before_install", "install", "before_script", "script"]:
            commands = project_config.get_list(name, [])
            yield Step(name, commands)
            
            
class Step(object):
    def __init__(self, name, commands):
        self.name = name
        self.commands = commands
