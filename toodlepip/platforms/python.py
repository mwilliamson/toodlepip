import os

from ..temp import create_temp_dir


class PythonBuilder(object):
    def __init__(self, console):
        self._console = console

    def matrix(self, project_config):
        return project_config.get_list("python", ["2.7"])
    
    def create_runtime(self, project_dir, entry):
        python_version = entry
        temp_dir = create_temp_dir()
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
