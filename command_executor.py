import subprocess


class CommandExecutor(object):
    def execute(self, command, env_var):
        subprocess.Popen(command.split(' '), env=env_var)
