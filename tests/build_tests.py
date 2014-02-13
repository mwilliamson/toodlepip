import io

import spur
from nose.tools import istest, assert_equal

from toodlepip.build import create_builder, Builder, StepRunner
from toodlepip.config import TravisConfig
from toodlepip.consoles import Console
from toodlepip import consoles
from toodlepip.platforms import DefaultBuilder
from . import testing


@istest
class BuilderTests(object):
    def __init__(self):
        self._stdout = io.BytesIO()
        shell = spur.LocalShell()
        console = Console(shell, self._stdout)
        self._builder = Builder({None: DefaultBuilder}, console)
    
    @property
    def _output(self):
        return self._stdout.getvalue()
    
    @istest
    def output_and_return_code_are_captured_by_build(self):
        result = self._build_empty(travis_yml={"script": "echo 'Hello, world!'"})
        assert b"Hello, world!" in self._output, "Output was: {0}".format(self._output)
        assert_equal(0, result.return_code)


    @istest
    def return_code_is_same_as_return_code_of_failed_command(self):
        result = self._build_empty(travis_yml={"script": "exit 1"})
        assert_equal(1, result.return_code)


    def _build_empty(self, travis_yml):
        with testing.create_project(travis_yml) as project:
            return self._builder.build(project.path)


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


@istest
class StepRunnerTests(object):
    @istest
    def all_steps_except_failure_are_executed_if_all_steps_are_successful(self):
        project_config = TravisConfig({})
        result = self._run_steps(project_config)
        
        assert_equal(0, result.return_code)
        
        success_steps = ["before_install", "install", "before_script", "script", "after_success", "after_script"]
        assert_equal(success_steps, self._executed_steps())

    @istest
    def if_script_command_has_non_zero_return_code_then_after_failure_is_run(self):
        project_config = TravisConfig({"script": ["exit 5"]})
        result = self._run_steps(project_config)
        
        assert_equal(5, result.return_code)
        
        assert_equal(
            ["before_install", "install", "before_script", "script", "after_failure", "after_script"],
            self._executed_steps()
        )

    @istest
    def execution_stops_if_step_before_script_command_has_non_zero_return_code(self):
        project_config = TravisConfig({"install": ["exit 5"]})
        result = self._run_steps(project_config)
        
        assert_equal(5, result.return_code)
        
        assert_equal(["before_install", "install"], self._executed_steps())

    @istest
    def return_code_is_zero_even_if_after_success_fails(self):
        project_config = TravisConfig({"after_success": ["exit 5"]})
        result = self._run_steps(project_config)
        
        assert_equal(0, result.return_code)
        
    def _run_steps(self, project_config):
        self._commands_runner = FakeCommandsRunner()
        runner = StepRunner(self._commands_runner)
        return runner.run_steps(project_config)
        
    def _executed_steps(self):
        return [step.name for step in self._commands_runner.steps]


class FakeCommandsRunner(object):
    def __init__(self):
        self.steps = []
    
    def run_commands(self, step):
        self.steps.append(step)
        if len(step.commands) > 0:
            return_code = step.commands[0].split(" ")[1]
            return consoles.Result(int(return_code))
        else:
            return consoles.Result(0)
