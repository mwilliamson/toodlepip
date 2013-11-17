import io

import spur
from nose.tools import istest, assert_equal

from toodlepip.consoles import Console


@istest
def console_writes_output_to_console():
    console, output = _create_local_console()
    console.run("Action", ["echo", "Go go go!"])
    assert b"Go go go!" in output.getvalue()


def _create_local_console():
    output = io.BytesIO()
    shell = spur.LocalShell()
    return Console(shell, output), output
    
