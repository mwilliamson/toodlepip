import tempfile
import shutil
import os

from . import config


class Builder(object):
    def __init__(self, shell, stdout):
        self._shell = shell
        self._stdout = stdout
    
    def build(self, path):
        project_config = config.read(path)
        
        working_dir = tempfile.mkdtemp()
        try:
            project_dir = os.path.join(working_dir, "project")
            virtualenv_dir = os.path.join(working_dir, "virtualenv")
            self._shell.run([
                "cp", "-r",
                path,
                project_dir,
            ])
            self._create_virtualenv(virtualenv_dir)
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
            _virtual_env_run(project_config.script)
        finally:
            shutil.rmtree(working_dir)
    
    def _run(self, *args, **kwargs):
        return self._shell.run(*args, stdout=self._stdout, **kwargs)
            
    def _create_virtualenv(self, path):
        self._shell.run(["virtualenv", path])
        
        def _pip_upgrade(package_name):
            pip = os.path.join(path, "bin", "pip")
            self._shell.run([pip, "install", "--upgrade", package_name])
        
        _pip_upgrade("pip")
        _pip_upgrade("setuptools")
        
