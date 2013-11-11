import tempfile
import shutil
import os

from . import config


class PythonBuilder(object):
    def __init__(self, console):
        self._console = console

    def matrix(self, project_config):
        return project_config.get_list("python", ["2.7"])

    def build(self, path, project_config, python_version):
        working_dir = tempfile.mkdtemp()
        try:
            project_dir = os.path.join(working_dir, "project")
            virtualenv_dir = os.path.join(working_dir, "virtualenv")
            self._console.run(
                "Copying project",
                ["cp", "-r", path, project_dir,],
                quiet=True,
            )
            self._create_virtualenv(virtualenv_dir, python_version)
            virtualenv_activate = os.path.join(virtualenv_dir, "bin/activate")
            
            def _virtualenv_run_all(description, commands):
                commands = map(_virtualenv_command, commands)
                self._console.run_all(
                    description,
                    commands,
                    cwd=project_dir
                )
            
            def _virtualenv_command(command):
                return [
                    "sh", "-c",
                    ". {0}; {1}".format(virtualenv_activate, command)
                ]
            
            _virtualenv_run_all("Running install commands", project_config.install)
            _virtualenv_run_all("Running script commands", project_config.script)
        finally:
            shutil.rmtree(working_dir)
    
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


class Builder(object):
    _builders = {
        "python": PythonBuilder
    }
        
    def __init__(self, shell, stdout):
        self._shell = shell
        self._stdout = stdout
    
    def build(self, path):
        project_config = config.read(path)
        
        language = project_config.language
        console = Console(self._shell, self._stdout)
        language_builder = self._builders[project_config.language](console)
        
        for entry in language_builder.matrix(project_config):
            language_builder.build(path, project_config, entry)
        

class Console(object):
    def __init__(self, shell, stdout):
        self._shell = shell
        self._stdout = stdout
        
    def run(self, description, command, **kwargs):
        return self.run_all(description, [command], **kwargs)
        
    def run_all(self, description, commands, quiet=False, cwd=None):
        stdout = None if quiet else self._stdout
        # TODO: Test printing description
        # TODO: detect terminal
        # TODO: stderr
        self._stdout.write('\033[1m')
        self._stdout.write(description)
        self._stdout.write("\n")
        self._stdout.write('\033[0m')
        self._stdout.flush()
        for command in commands:
            # TODO: print command
            self._shell.run(command, stdout=stdout, cwd=cwd)
