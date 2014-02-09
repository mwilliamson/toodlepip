from nose.tools import istest, assert_equal
import spur

from . import testing


local = spur.LocalShell()


@istest
def build_command_builds_project_locally():
    result = local.run(["toodlepip", "build", testing.path("travis-minimal")])
    assert b"Hello, world!" in result.output, "Output was: {0}".format(result.output)
    assert_equal(0, result.return_code)
