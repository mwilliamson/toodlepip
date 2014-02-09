import os

from nose.tools import istest, assert_equal
import spur
import tempman
import yaml

from . import testing


local = spur.LocalShell()


@istest
def build_command_builds_project_locally():
    result = _build_empty(travis_yml={"script": "echo 'Hello, world!'"})
    assert b"Hello, world!" in result.output, "Output was: {0}".format(result.output)
    assert_equal(0, result.return_code)


def _build_empty(travis_yml):
    with tempman.create_temp_dir() as temp_dir:
        with open(os.path.join(temp_dir.path, ".travis.yml"), "w") as travis_yml_file:
            yaml.dump(travis_yml, travis_yml_file)
        return local.run(["toodlepip", "build", temp_dir.path])
