from . import config, files
from .consoles import Console, Command
from .platforms import builders
from .temp import create_temp_dir


def create_builder(shell, stdout):
    return Builder(builders, Console(shell, stdout))


class Builder(object):
    def __init__(self, builders, console):
        self._console = console
        self._builders = builders
    
    def build(self, path):
        with create_temp_dir() as temp_dir:
            project_dir = temp_dir.path
            self._console.run_all(
                "Copying project",
                [],
                quiet=True,
            )
            files.copy(path, project_dir)
        
            project_config = config.read(path)
            
            language_builder = self._builders[project_config.language](self._console)
            
            for entry in language_builder.matrix(project_config):
                result = self._build_entry(language_builder, project_dir, project_config, entry)
                if result.return_code != 0:
                    return BuildResult(result.return_code)
            
            return BuildResult(0)
            
    def _build_entry(self, language_builder, project_dir, project_config, entry):
        with language_builder.create_runtime(project_dir, entry) as runtime:
            step_runner = StepRunner(CommandsRunner(self._console, runtime, project_dir))
            return step_runner.run_steps(project_config)
            
            
class StepRunner(object):
    def __init__(self, commands_runner):
        self._commands_runner = commands_runner
    
    def run_steps(self, project_config):
        for step_name in ["before_install", "install", "before_script"]:
            result = self._run_step(project_config, step_name)
            if result.return_code != 0:
                return result
                
        result = self._run_step(project_config, "script")
        if result.return_code == 0:
            after_step = "after_success"
        else:
            after_step = "after_failure"
            
        self._run_step(project_config, after_step)
        self._run_step(project_config, "after_script")
        
        return result
        
    def _run_step(self, project_config, step_name):
        step = self._step(project_config, step_name)
        return self._commands_runner.run_commands(step)
        
    def _step(self, project_config, name):
        commands = project_config.get_list(name, [])
        return Step(name, commands)


class CommandsRunner(object):
    def __init__(self, console, runtime, project_dir):
        self._console = console
        self._runtime = runtime
        self._project_dir = project_dir
    
    def run_commands(self, step):
        def _runtime_run_all(description, commands):
            commands = map(_runtime_command, commands)
            return self._console.run_all(
                description,
                commands,
                cwd=self._project_dir
            )
        
        def _runtime_command(command):
            before_command = self._runtime.before_step(step)
            if before_command:
                return Command.hidden_prefix(command, prefix=before_command)
            else:
                return Command.shell(command)
        
        return _runtime_run_all("Running {0} commands".format(step.name), step.commands)
        

            
class Step(object):
    def __init__(self, name, commands):
        self.name = name
        self.commands = commands


class BuildResult(object):
    def __init__(self, return_code):
        self.return_code = return_code
