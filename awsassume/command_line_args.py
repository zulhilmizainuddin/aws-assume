import argparse

from data_models import CliArgs


class CommandLineArgs(object):
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description='AWS assume role')

        self.parser.add_argument('--role-arn', required=True)
        self.parser.add_argument('--role-session-name', required=True)
        self.parser.add_argument('--command', required=False, nargs='*')
        self.parser.add_argument('--region-name', required=False)
        self.parser.add_argument('--no-cache', required=False, action='store_true')

    def get_cli_args(self) -> CliArgs:

        parsed_cli_args: argparse.Namespace = self.parser.parse_args()

        cli_args = CliArgs(role_arn=parsed_cli_args.role_arn,
                           role_session_name=parsed_cli_args.role_session_name,
                           command=parsed_cli_args.command,
                           region_name=parsed_cli_args.region_name,
                           no_cache=parsed_cli_args.no_cache)

        return cli_args
