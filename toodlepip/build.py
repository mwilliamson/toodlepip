import os
from datetime import timedelta

import tempman
import xdg.BaseDirectory

from . import config, files
from .consoles import Console, Result


class DefaultBuilder(object):
    def __init__(self, console):
        self._console = console
    
    def matrix(self, project_config):
        return [None]
    
    def create_runtime(self, project_dir, entry):
        return DefaultRuntime()


class DefaultRuntime(object):
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        return
    
    def before_step(self, step):
        return None


class PythonBuilder(object):
    def __init__(self, console):
        self._console = console

    def matrix(self, project_config):
        return project_config.get_list("python", ["2.7"])
    
    def create_runtime(self, project_dir, entry):
        python_version = entry
        temp_dir = _create_temp_dir()
        try:
            working_dir = temp_dir.path
            virtualenv_dir = os.path.join(working_dir, "virtualenv")
            self._create_virtualenv(virtualenv_dir, python_version)
        except Exception:
            temp_dir.close()
            raise
        return PythonRuntime(temp_dir, virtualenv_dir)
    
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
            "Creating virtualenv for {0}".format(python_version),
            commands,
            quiet=True,
        )
        
        
    def _python_binary(self, python_version):
        if python_version == "pypy":
            return "pypy"
        else:
            return "python{0}".format(python_version)


class PythonRuntime(object):
    def __init__(self, temp_dir, virtualenv_dir):
        self._temp_dir = temp_dir
        self._virtualenv_dir = virtualenv_dir
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self._temp_dir.close()

    def before_step(self, step):
        virtualenv_activate = os.path.join(self._virtualenv_dir, "bin/activate")
        return ". {0}".format(virtualenv_activate)


_default_builders = {
    None: DefaultBuilder,
    "python": PythonBuilder,
}

def create_builder(shell, stdout):
    return Builder(_default_builders, Console(shell, stdout))


class Builder(object):
    def __init__(self, builders, console):
        self._console = console
        self._builders = builders
    
    def build(self, path):
        with _create_temp_dir() as temp_dir:
            project_dir = temp_dir.path
            self._console.run_all(
                "Copying project",
                [],
                quiet=True,
            )
            files.copy(path, project_dir)
        
            project_config = config.read(path)
            
            language = project_config.language
            language_builder = self._builders[project_config.language](self._console)
            
            for entry in language_builder.matrix(project_config):
                result = self._build_entry(language_builder, project_dir, project_config, entry)
                if result.return_code != 0:
                    return result.return_code
            
            return 0
            
    def _build_entry(self, language_builder, project_dir, project_config, entry):
        with language_builder.create_runtime(project_dir, entry) as runtime:
            step_runner = StepRunner(CommandsRunner(self._console, runtime, project_dir))
            return step_runner.run_steps(project_config)
            
            
class StepRunner(object):
    def __init__(self, commands_runner):
        self._commands_runner = commands_runner
    
    def run_steps(self, project_config):
        for step_name in ["before_install", "install", "before_script"]:
            result = self._run_step(project_config, step_name)
            if result.return_code != 0:
                return result
                
        result = self._run_step(project_config, "script")
        if result.return_code == 0:
            after_step = "after_success"
        else:
            after_step = "after_failure"
            
        self._run_step(project_config, after_step)
        self._run_step(project_config, "after_script")
        
        return result
        
    def _run_step(self, project_config, step_name):
        step = self._step(project_config, step_name)
        return self._commands_runner.run_commands(step)
        
    def _step(self, project_config, name):
        commands = project_config.get_list(name, [])
        return Step(name, commands)


class CommandsRunner(object):
    def __init__(self, console, runtime, project_dir):
        self._console = console
        self._runtime = runtime
        self._project_dir = project_dir
    
    def run_commands(self, step):
        def _runtime_run_all(description, commands):
            commands = map(_runtime_command, commands)
            return self._console.run_all(
                description,
                commands,
                cwd=self._project_dir
            )
        
        def _runtime_command(command):
            before_command = self._runtime.before_step(step) or "true"
            return [
                "sh", "-c",
                "{0}; {1}".format(before_command, command)
            ]
        
        return _runtime_run_all("Running {0} commands".format(step.name), step.commands)
        

            
class Step(object):
    def __init__(self, name, commands):
        self.name = name
        self.commands = commands

    
def _create_temp_dir():
    temp_root = tempman.root(
        xdg.BaseDirectory.save_data_path("toodlepip/tmp"),
        timeout=timedelta(days=1)
    )
    return temp_root.create_temp_dir()
