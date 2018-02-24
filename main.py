#!/usr/bin/env python3

from assume_role import AssumeRole
from command_executor import CommandExecutor
from command_line_args import CommandLineArgs
from data_models import AssumeRoleArgs, AWSCredentials
from environment_variable import EnvironmentVariable

# temp for testing
from test.fixture.response import assume_role_response
# temp for testing

if __name__ == '__main__':
    cli_args = CommandLineArgs().get_cli_args()

    assume_role_args = AssumeRoleArgs(role_arn=cli_args.role_arn, role_session_name=cli_args.role_session_name)
    aws_credentials = AssumeRole().assume_role(assume_role_args)

    # temp for testing
    # aws_credentials = AWSCredentials(access_key_id=assume_role_response['Credentials']['AccessKeyId'],
    #                                  secret_access_key=assume_role_response['Credentials']['SecretAccessKey'],
    #                                  session_token=assume_role_response['Credentials']['SessionToken'],
    #                                  expiration=assume_role_response['Credentials']['Expiration'].isoformat())
    # temp for testing

    if cli_args.command is None:
        print('# AWS assumed role credentials:')
        print(f'# {EnvironmentVariable.ACCESS_KEY_ID_KEY}={aws_credentials.access_key_id}')
        print(f'# {EnvironmentVariable.SECRET_ACCESS_KEY_KEY}={aws_credentials.secret_access_key}')
        print(f'# {EnvironmentVariable.SESSION_TOKEN_KEY}={aws_credentials.session_token}')
        print(f'# {EnvironmentVariable.SESSION_TOKEN_EXPIRATION_KEY}={aws_credentials.expiration}')

        print()

        print('# Execute the following command to export the AWS assumed role credentials to environment variables.')

        command_to_eval = EnvironmentVariable.generate_command_to_export_aws_credentials(aws_credentials)
        print(command_to_eval)
    else:
        env_var_with_aws_credentials = EnvironmentVariable.get_env_var_with_aws_credentials(aws_credentials)

        CommandExecutor().execute(cli_args.command, env_var_with_aws_credentials)