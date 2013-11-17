class Console(object):
    def __init__(self, shell, stdout):
        self._shell = shell
        self._stdout = stdout
        
    def run(self, description, command, **kwargs):
        return self.run_all(description, [command], **kwargs)
        
    def run_all(self, description, commands, quiet=False, cwd=None):
        stdout = None if quiet else self._stdout
        # TODO: Test printing description
        # TODO: detect terminal
        self._stdout.write('\033[1m')
        self._stdout.write(description)
        self._stdout.write("\n")
        self._stdout.write('\033[0m')
        self._stdout.flush()
        for command in commands:
            # TODO: print command
            self._shell.run(command, stdout=stdout, stderr=stdout, cwd=cwd)
