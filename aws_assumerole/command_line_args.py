import argparse


class CommandLineArgs(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='AWS assume role')

        self.parser.add_argument('--role-arn', required=True)
        self.parser.add_argument('--role-session-name', required=True)
        self.parser.add_argument('--command', required=False)

    def get_cli_args(self):
        return self.parser.parse_args()
