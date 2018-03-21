#!/usr/bin/env python3

from assume_role import AssumeRole
from assume_role_cache_executor import AssumeRoleCacheExecutor
from assume_role_executor import AssumeRoleExecutor
from assume_role_no_cache_executor import AssumeRoleNoCacheExecutor
from assumed_role_response_cache import AssumedRoleResponseCache
from command_executor import CommandExecutor
from command_line_args import CommandLineArgs
from data_models import AssumeRoleArgs, CliArgs, Credentials
from environment_variable import EnvironmentVariable
from security_token_service import SecurityTokenService

if __name__ == '__main__':
    cli_args: CliArgs = CommandLineArgs().get_cli_args()

    assume_role_args = AssumeRoleArgs(role_arn=cli_args.role_arn, role_session_name=cli_args.role_session_name, region_name=cli_args.region_name)
    security_token_service: SecurityTokenService = AssumeRole(assume_role_args)

    assume_role_executor: AssumeRoleExecutor = None
    if cli_args.no_cache is True:
        assume_role_executor = AssumeRoleNoCacheExecutor(security_token_service)
    else:
        assumed_role_response_cache = AssumedRoleResponseCache(cli_args.role_arn, cli_args.role_session_name, cli_args.region_name)
        assume_role_executor = AssumeRoleCacheExecutor(security_token_service, assumed_role_response_cache)

    credentials: Credentials = assume_role_executor.execute()

    if cli_args.command is None:
        print('# AWS assumed role credentials:')
        EnvironmentVariable.display_credentials_to_be_exported(credentials, cli_args.region_name)

        print()

        print('# Execute the following command to export the AWS assumed role credentials to environment variables.')

        command_to_eval = EnvironmentVariable.generate_command_to_export_credentials(credentials, cli_args.region_name)
        print(command_to_eval)
    else:
        env_var_with_credentials = EnvironmentVariable.get_env_var_with_credentials(credentials, cli_args.region_name)

        CommandExecutor().execute(cli_args.command, env_var_with_credentials)
