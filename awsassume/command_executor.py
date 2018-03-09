import subprocess

from typing import Dict


class CommandExecutor(object):
    def execute(self, command: str, env_var: Dict[str, str]) -> None:
        subprocess.Popen(command.split(' '), env=env_var)
