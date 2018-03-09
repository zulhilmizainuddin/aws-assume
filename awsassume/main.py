#!/usr/bin/env python3

from assume_role import AssumeRole
from command_executor import CommandExecutor
from command_line_args import CommandLineArgs
from data_models import AssumeRoleArgs, AssumedRoleResponse
from environment_variable import EnvironmentVariable

if __name__ == '__main__':
    cli_args = CommandLineArgs().get_cli_args()

    assume_role_args = AssumeRoleArgs(role_arn=cli_args.role_arn, role_session_name=cli_args.role_session_name)
    assumed_role_response: AssumedRoleResponse = AssumeRole().assume_role(assume_role_args)

    if cli_args.command is None:
        print('# AWS assumed role credentials:')
        print(f'# {EnvironmentVariable.ACCESS_KEY_ID_KEY}={assumed_role_response.credentials.access_key_id}')
        print(f'# {EnvironmentVariable.SECRET_ACCESS_KEY_KEY}={assumed_role_response.credentials.secret_access_key}')
        print(f'# {EnvironmentVariable.SESSION_TOKEN_KEY}={assumed_role_response.credentials.session_token}')
        print(f'# {EnvironmentVariable.SESSION_TOKEN_EXPIRATION_KEY}={assumed_role_response.credentials.expiration.isoformat()}')

        print()

        print('# Execute the following command to export the AWS assumed role credentials to environment variables.')

        command_to_eval = EnvironmentVariable.generate_command_to_export_aws_credentials(assumed_role_response.credentials)
        print(command_to_eval)
    else:
        env_var_with_aws_credentials = EnvironmentVariable.get_env_var_with_aws_credentials(assumed_role_response.credentials)

        CommandExecutor().execute(cli_args.command, env_var_with_aws_credentials)