from nose.tools import istest, assert_equal

from toodlepip import config
from . import testing


@istest
def script_command_is_read_from_travis_yml():
    project_config = config.read(testing.path("minimal-python"))
    assert_equal("greet", project_config.script)


@istest
def install_command_is_read_from_travis_yml():
    project_config = config.read(testing.path("minimal-python"))
    assert_equal(["pip install . --use-mirrors"], project_config.install)
