import os

import yaml


def read(path):
    with open(os.path.join(path, ".travis.yml")) as yml_file:
        return _read_travis_yml(yml_file)


def _read_travis_yml(yml_file):
    config = yaml.load(yml_file)
    return TravisConfig(config)


class TravisConfig(object):
    def __init__(self, yaml):
        self._yaml = yaml
        
    @property
    def script(self):
        return self._yaml["script"]

    @property
    def install(self):
        return self._yaml["install"]
