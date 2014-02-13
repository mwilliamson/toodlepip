class DefaultBuilder(object):
    def __init__(self, console):
        self._console = console
    
    def matrix(self, project_config):
        return [None]
    
    def create_runtime(self, project_dir, entry):
        return DefaultRuntime()


class DefaultRuntime(object):
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        return
    
    def before_step(self, step):
        return None
