from nose.tools import istest, assert_in, assert_equal
import spur

from . import testing


local = spur.LocalShell()


@istest
def python_project_configured_with_travis_yml_can_be_built():
    result = local.run(["toodlepip", "build", testing.path("minimal-python")])
    assert_in("This is Python 2.7 calling", result.output)
    assert_equal(0, result.return_code)

