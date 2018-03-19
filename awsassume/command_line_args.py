import argparse


class CommandLineArgs(object):
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description='AWS assume role')

        self.parser.add_argument('--role-arn', required=True)
        self.parser.add_argument('--role-session-name', required=True)
        self.parser.add_argument('--command', required=False)
        self.parser.add_argument('--no-cache', required=False, action='store_true')

    def get_cli_args(self) -> argparse.Namespace:
        return self.parser.parse_args()
