import argparse
import pytest

from command_line_args import CommandLineArgs
from data_models import CliArgs
from unittest.mock import MagicMock


@pytest.fixture(scope='module')
def command_line_args():
    return CommandLineArgs()


@pytest.fixture(scope='module')
def passed_cli_args():
    cli_args = argparse.Namespace()
    cli_args.role_arn = 'arn:aws:iam::123456789012:role/rolename'
    cli_args.role_session_name = 'sessionname'
    cli_args.command = 'aws s3 ls'
    cli_args.region_name = 'ap-southeast-1'
    cli_args.no_cache = False

    return cli_args


@pytest.fixture(scope='module')
def parsed_cli_args():
    return CliArgs(role_arn='arn:aws:iam::123456789012:role/rolename',
                   role_session_name='sessionname',
                   command='aws s3 ls',
                   region_name='ap-southeast-1',
                   no_cache=False)


def test_get_cli_args(command_line_args, passed_cli_args, parsed_cli_args):
    command_line_args.parser.parse_args = MagicMock(return_value=passed_cli_args)

    assert command_line_args.get_cli_args() == parsed_cli_args
