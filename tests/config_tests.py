import io

from nose.tools import istest, assert_equal

from toodlepip import config
from . import testing


@istest
def config_read_from_travis_yml_for_project_if_present():
    project_config = config.read(testing.path("minimal-python"))
    assert_equal("python", project_config.language)


@istest
def language_is_read_from_travis_yml():
    yaml_file = io.BytesIO(b"language: python")
    project_config = config.read_travis_yml(yaml_file)
    assert_equal("python", project_config.language)


@istest
def script_command_is_read_from_travis_yml():
    yaml_file = io.BytesIO(b"script: greet")
    project_config = config.read_travis_yml(yaml_file)
    assert_equal(["greet"], project_config.script)


@istest
def install_command_is_read_from_travis_yml():
    yaml_file = io.BytesIO(b"install:\n- pip install . --use-mirrors")
    project_config = config.read_travis_yml(yaml_file)
    assert_equal(["pip install . --use-mirrors"], project_config.install)


@istest
def get_list_returns_none_if_key_not_present():
    yaml_file = io.BytesIO(b"language: python")
    project_config = config.read_travis_yml(yaml_file)
    assert_equal(None, project_config.get_list("python"))


@istest
def get_list_returns_default_if_key_not_present_and_default_is_provided():
    yaml_file = io.BytesIO(b"language: python")
    project_config = config.read_travis_yml(yaml_file)
    assert_equal(["2.7"], project_config.get_list("python", ["2.7"]))


@istest
def get_list_returns_singleton_list_if_value_is_string():
    yaml_file = io.BytesIO(b'language: python\npython: "2.7"')
    project_config = config.read_travis_yml(yaml_file)
    assert_equal(["2.7"], project_config.get_list("python"))


@istest
def get_list_returns_list_if_key_is_present():
    yaml_file = io.BytesIO(b'language: python\npython:\n- "2.6"\n- "2.7"')
    project_config = config.read_travis_yml(yaml_file)
    assert_equal(["2.6", "2.7"], project_config.get_list("python"))

