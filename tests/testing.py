import os

import yaml
import tempman


def path(path):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(this_dir, "../test-files", path)


def create_project(travis_yml):
    temp_dir = tempman.create_temp_dir()
    try:
        with open(os.path.join(temp_dir.path, ".travis.yml"), "w") as travis_yml_file:
            yaml.dump(travis_yml, travis_yml_file)
    except Exception:
        temp_dir.close()
        raise
    return Project(temp_dir)


class Project(object):
    def __init__(self, temp_dir):
        self._temp_dir = temp_dir
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self._temp_dir.close()
    
    @property
    def path(self):
        return self._temp_dir.path
