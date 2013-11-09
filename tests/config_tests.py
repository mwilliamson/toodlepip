import io

from nose.tools import istest, assert_equal

from toodlepip import config
from . import testing


@istest
def config_read_from_travis_yml_for_project_if_present():
    project_config = config.read(testing.path("minimal-python"))
    assert_equal("greet", project_config.script)


@istest
def script_command_is_read_from_travis_yml():
    yaml_file = io.BytesIO(b"script: greet")
    project_config = config.read_travis_yml(yaml_file)
    assert_equal("greet", project_config.script)


@istest
def install_command_is_read_from_travis_yml():
    yaml_file = io.BytesIO(b"install:\n- pip install . --use-mirrors")
    project_config = config.read_travis_yml(yaml_file)
    assert_equal(["pip install . --use-mirrors"], project_config.install)
