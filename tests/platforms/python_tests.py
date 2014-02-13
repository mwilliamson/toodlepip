import io

import spur
from nose.tools import istest

from toodlepip.build import create_builder
from .. import testing


@istest
class PythonBuilderTests(object):
    def __init__(self):
        self._stdout = io.BytesIO()
        shell = spur.LocalShell()
        self._builder = create_builder(shell, self._stdout)
    
    @istest
    def python_project_configured_with_travis_yml_can_be_built(self):
        self._builder.build(testing.path("minimal-python"))
        self._assert_stdout_contains(b"This is CPython 2.7 calling")


    @istest
    def stderr_output_is_captured(self):
        self._builder.build(testing.path("minimal-python-stderr"))
        self._assert_stdout_contains(b"This is CPython 2.7 calling")


    @istest
    def python_version_can_be_selected(self):
        self._builder.build(testing.path("minimal-python-2.6"))
        self._assert_stdout_contains(b"This is CPython 2.6 calling")


    @istest
    def pypy_can_be_used_as_python_version(self):
        self._builder.build(testing.path("minimal-python-pypy"))
        self._assert_stdout_contains(b"This is PyPy 2.7 calling")
        
    
    def _assert_stdout_contains(self, expected):
        output = self._stdout.getvalue()
        assert expected in output, "Output was: {0}".format(output)
