#!/usr/bin/env python3

import argparse

from assume_role import AssumeRole
from assume_role_cache_executor import AssumeRoleCacheExecutor
from assume_role_executor import AssumeRoleExecutor
from assume_role_no_cache_executor import AssumeRoleNoCacheExecutor
from command_executor import CommandExecutor
from command_line_args import CommandLineArgs
from data_models import AssumeRoleArgs, Credentials
from environment_variable import EnvironmentVariable
from security_token_service import SecurityTokenService

if __name__ == '__main__':
    cli_args: argparse.Namespace = CommandLineArgs().get_cli_args()

    assume_role_args = AssumeRoleArgs(role_arn=cli_args.role_arn, role_session_name=cli_args.role_session_name)
    security_token_service: SecurityTokenService = AssumeRole(assume_role_args, cli_args.region)

    assume_role_executor: AssumeRoleExecutor = None
    if cli_args.no_cache is True:
        assume_role_executor = AssumeRoleNoCacheExecutor(security_token_service)
    else:
        assume_role_executor = AssumeRoleCacheExecutor(cli_args.role_arn, cli_args.role_session_name, security_token_service)

    credentials: Credentials = assume_role_executor.execute()

    if cli_args.command is None:
        print('# AWS assumed role credentials:')
        print(f'# {EnvironmentVariable.ACCESS_KEY_ID_KEY}={credentials.access_key_id}')
        print(f'# {EnvironmentVariable.SECRET_ACCESS_KEY_KEY}={credentials.secret_access_key}')
        print(f'# {EnvironmentVariable.SESSION_TOKEN_KEY}={credentials.session_token}')

        print()

        print('# Execute the following command to export the AWS assumed role credentials to environment variables.')

        command_to_eval = EnvironmentVariable.generate_command_to_export_aws_credentials(credentials)
        print(command_to_eval)
    else:
        env_var_with_aws_credentials = EnvironmentVariable.get_env_var_with_aws_credentials(credentials)

        CommandExecutor().execute(cli_args.command, env_var_with_aws_credentials)
