import io

import spur
from nose.tools import istest, assert_equal

from toodlepip.consoles import Console


@istest
def console_writes_stdout_output_to_console():
    console, output = _create_local_console()
    console.run(None, ["echo", "Go go go!"])
    assert_equal("Go go go!\n", output.getvalue())


@istest
def console_writes_stderr_output_to_console():
    console, output = _create_local_console()
    console.run(None, ["sh", "-c", "echo 'Go go go!' 1>&2"])
    assert_equal("Go go go!\n", output.getvalue())


@istest
def return_code_is_zero_if_all_commands_are_successful():
    console, output = _create_local_console()
    result = console.run_all("Action", [["true"]])
    assert_equal(0, result.return_code)


@istest
def return_code_is_first_non_zero_return_code_of_commands():
    console, output = _create_local_console()
    result = console.run_all("Action", [["true"], ["sh", "-c", "exit 2"], ["true"], ["sh", "-c", "exit 1"]])
    assert_equal(2, result.return_code)


def _create_local_console():
    output = io.BytesIO()
    shell = spur.LocalShell()
    return Console(shell, output), output
    
