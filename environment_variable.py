import os


class EnvironmentVariable(object):

    ACCESS_KEY_ID_KEY = 'AWS_ACCESS_KEY_ID'
    SECRET_ACCESS_KEY_KEY = 'AWS_SECRET_ACCESS_KEY'
    SESSION_TOKEN_KEY = 'AWS_SESSION_TOKEN'
    SESSION_TOKEN_EXPIRATION_KEY = 'AWS_SESSION_TOKEN_EXPIRATION'

    @staticmethod
    def generate_command_to_export_aws_credentials(aws_credentials):

        export_access_key_id =\
            f'export {EnvironmentVariable.ACCESS_KEY_ID_KEY}="{aws_credentials.access_key_id}"'
        export_secret_access_key =\
            f'export {EnvironmentVariable.SECRET_ACCESS_KEY_KEY}="{aws_credentials.secret_access_key}"'
        export_session_token =\
            f'export {EnvironmentVariable.SESSION_TOKEN_KEY}="{aws_credentials.session_token}"'
        export_expiration =\
            f'export {EnvironmentVariable.SESSION_TOKEN_EXPIRATION_KEY}="{aws_credentials.expiration}"'

        command =\
            f'eval "{export_access_key_id}; {export_secret_access_key}; {export_session_token}; {export_expiration}"'

        return command

    @staticmethod
    def get_env_var_with_aws_credentials(aws_credentials):
        env_var_copy = os.environ.copy()

        env_var_copy[EnvironmentVariable.ACCESS_KEY_ID_KEY] = aws_credentials.access_key_id
        env_var_copy[EnvironmentVariable.SECRET_ACCESS_KEY_KEY] = aws_credentials.secret_access_key
        env_var_copy[EnvironmentVariable.SESSION_TOKEN_KEY] = aws_credentials.session_token
        env_var_copy[EnvironmentVariable.SESSION_TOKEN_EXPIRATION_KEY] = aws_credentials.expiration

        return env_var_copy
