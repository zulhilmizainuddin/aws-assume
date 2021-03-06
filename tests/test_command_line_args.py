import argparse
import pytest

from unittest.mock import MagicMock

from awsassume.command_line_args import CommandLineArgs
from awsassume.data_models import CliArgs


@pytest.fixture(scope='module')
def command_line_args():
    return CommandLineArgs()


@pytest.fixture(scope='module')
def argparse_cli_args():
    cli_args = argparse.Namespace()
    cli_args.role_arn = 'arn:aws:iam::123456789012:role/rolename'
    cli_args.role_session_name = 'sessionname'
    cli_args.command = 'aws s3 ls'
    cli_args.region = 'ap-southeast-1'
    cli_args.no_cache = False

    return cli_args


@pytest.fixture(scope='module')
def cli_args():
    return CliArgs(role_arn='arn:aws:iam::123456789012:role/rolename',
                   role_session_name='sessionname',
                   command='aws s3 ls',
                   region_name='ap-southeast-1',
                   no_cache=False)


def test_get_cli_args(command_line_args, argparse_cli_args, cli_args):
    command_line_args.parser.parse_args = MagicMock(return_value=argparse_cli_args)

    assert command_line_args.get_cli_args() == cli_args
