import io

import spur
from nose.tools import istest, assert_equal

from toodlepip.consoles import Console, Command


@istest
def console_writes_stdout_output_to_console():
    console, output = _create_local_console()
    console.run(None, Command.shell("echo Go go go!"))
    assert_equal(b"$ echo Go go go!\nGo go go!\n", output.getvalue())


@istest
def console_writes_stderr_output_to_console():
    console, output = _create_local_console()
    console.run(None, Command.shell("echo 'Go go go!' 1>&2"))
    assert_equal(b"$ echo 'Go go go!' 1>&2\nGo go go!\n", output.getvalue())


@istest
def console_writes_description_before_command_output():
    console, output = _create_local_console()
    console.run("Action", Command.shell("true"))
    assert_equal(b"\x1b[1mAction\n\x1b[0m$ true\n", output.getvalue())


@istest
def return_code_is_zero_if_all_commands_are_successful():
    console, output = _create_local_console()
    result = console.run_all("Action", [Command.shell("true")])
    assert_equal(0, result.return_code)


@istest
def return_code_is_first_non_zero_return_code_of_commands():
    console, output = _create_local_console()
    result = console.run_all("Action", map(Command.shell, ["true", "exit 2", "true", "exit 1"]))
    assert_equal(2, result.return_code)


@istest
def no_output_except_description_if_quiet_arg_is_set():
    console, output = _create_local_console()
    console.run("Action", Command.shell("echo Go go go!"), quiet=True)
    assert_equal(b"\x1b[1mAction\n\x1b[0m", output.getvalue())


def _create_local_console():
    output = io.BytesIO()
    shell = spur.LocalShell()
    return Console(shell, output), output
    
