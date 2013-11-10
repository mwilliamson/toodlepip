import tempfile
import shutil
import os

from . import config


class PythonBuilder(object):
    def __init__(self, shell, stdout):
        self._shell = shell
        self._stdout = stdout

    def matrix(self, project_config):
        return project_config.get_list("python", ["2.7"])

    def build(self, path, project_config, python_version):
        working_dir = tempfile.mkdtemp()
        try:
            project_dir = os.path.join(working_dir, "project")
            virtualenv_dir = os.path.join(working_dir, "virtualenv")
            self._shell.run([
                "cp", "-r",
                path,
                project_dir,
            ])
            self._create_virtualenv(virtualenv_dir, python_version)
            virtualenv_activate = os.path.join(virtualenv_dir, "bin/activate")
            
            def _virtual_env_run(command):
                self._run([
                    "sh", "-c",
                    _virtualenv_command(command)
                ], cwd=project_dir)
            
            def _virtualenv_command(command):
                return ". {0}; {1}".format(virtualenv_activate, command)
            
            for command in project_config.install:
                _virtual_env_run(command)
            for command in project_config.script:
                _virtual_env_run(command)
        finally:
            shutil.rmtree(working_dir)
    
    def _run(self, *args, **kwargs):
        return self._shell.run(*args, stdout=self._stdout, **kwargs)
            
    def _create_virtualenv(self, path, python_version):
        python_binary = self._python_binary(python_version)
        self._shell.run(["virtualenv", path, "--python={0}".format(python_binary)])
        
        def _pip_upgrade(package_name):
            pip = os.path.join(path, "bin", "pip")
            self._shell.run([pip, "install", "--upgrade", package_name])
        
        _pip_upgrade("pip")
        _pip_upgrade("setuptools")
        _pip_upgrade("virtualenv")
        
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
        language_builder = self._builders[project_config.language](self._shell, self._stdout)
        
        for entry in language_builder.matrix(project_config):
            language_builder.build(path, project_config, entry)
        
