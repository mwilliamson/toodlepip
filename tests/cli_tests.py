from nose.tools import istest, assert_equal
import spur

from . import testing


local = spur.LocalShell()


@istest
def python_project_configured_with_travis_yml_can_be_built():
    result = local.run(["toodlepip", "build", testing.path("minimal-python")])
    assert b"This is CPython 2.7 calling" in result.output, "Output was: {0}".format(result.output)
    assert_equal(0, result.return_code)


@istest
def python_version_can_be_selected():
    result = local.run(["toodlepip", "build", testing.path("minimal-python-2.6")])
    assert b"This is CPython 2.6 calling" in result.output, "Output was: {0}".format(result.output)
    assert_equal(0, result.return_code)


@istest
def pypy_can_be_used_as_python_version():
    result = local.run(["toodlepip", "build", testing.path("minimal-python-pypy")])
    assert b"This is PyPy 2.7 calling" in result.output, "Output was: {0}".format(result.output)
    assert_equal(0, result.return_code)
