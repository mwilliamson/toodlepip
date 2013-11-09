from nose.tools import istest, assert_equal
import spur

from . import testing


local = spur.LocalShell()


@istest
def python_project_configured_with_travis_yml_can_be_built():
    result = local.run(["toodlepip", "build", testing.path("minimal-python")])
    print(result.stderr_output)
    assert b"This is Python 2.7 calling" in result.output, "Output was: {0}".format(result.output)
    assert_equal(0, result.return_code)

