import pipes


class Console(object):
    def __init__(self, shell, stdout):
        self._shell = shell
        self._stdout = stdout
        
    def run(self, description, command, **kwargs):
        return self.run_all(description, [command], **kwargs)
        
    def run_all(self, description, commands, quiet=False, cwd=None, allow_error=True):
        self._write_description(description)
        for command in commands:
            if isinstance(command, list):
                command = _join_shell_args(command)
            
            if not quiet:
                self._write_command(command)
            
            process_stdout = None if quiet else self._stdout
            result = self._shell.run(
                ["sh", "-c", command],
                stdout=process_stdout,
                stderr=process_stdout,
                cwd=cwd,
                allow_error=allow_error,
            )
            if result.return_code != 0:
                return Result(result.return_code)
            
            
        return Result(0)
    
    def _write_description(self, description):
        if description:
            # TODO: detect terminal
            self._stdout.write(b'\033[1m')
            self._stdout.write(description.encode("utf8"))
            self._stdout.write(b"\n")
            self._stdout.write(b'\033[0m')
            self._stdout.flush()
    
    def _write_command(self, command):
        self._stdout.write(b"$ ")
        self._stdout.write(command.encode("utf8"))
        self._stdout.write(b"\n")


class Result(object):
    def __init__(self, return_code):
        self.return_code = return_code


def _join_shell_args(args):
    return " ".join([pipes.quote(arg) for arg in args])
