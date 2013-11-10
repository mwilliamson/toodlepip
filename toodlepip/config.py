import os
import sys

import yaml


def read(path):
    with open(os.path.join(path, ".travis.yml")) as yml_file:
        return read_travis_yml(yml_file)


def read_travis_yml(yml_file):
    config = yaml.load(yml_file)
    return TravisConfig(config)


class TravisConfig(object):
    def __init__(self, yaml):
        self._yaml = yaml
        
    @property
    def language(self):
        return self._yaml["language"]
        
    @property
    def script(self):
        return self.get_list("script")

    @property
    def install(self):
        return self.get_list("install")
        
    def get_list(self, name, default=None):
        value = self._yaml.get(name, default)
        if _is_string(value):
            return [value]
        else:
            return value


def _is_string(value):
    if sys.version_info[0] <= 2:
        string_cls = basestring
    else:
        string_cls = str
        
    return isinstance(value, string_cls)
