from nose.tools import istest, assert_equal
import spur

from . import testing


local = spur.LocalShell()


@istest
def build_command_builds_project_locally():
    result = _build_empty(travis_yml={"script": "echo 'Hello, world!'"})
    assert b"Hello, world!" in result.output, "Output was: {0}".format(result.output + result.stderr_output)
    assert_equal(0, result.return_code)


@istest
def return_code_is_same_as_return_code_of_failed_command():
    result = _build_empty(travis_yml={"script": "exit 1"})
    assert_equal(1, result.return_code)


def _build_empty(travis_yml):
    with testing.create_project(travis_yml) as project:
        return local.run(["toodlepip", "build", project.path], allow_error=True)
