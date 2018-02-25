from data_models import AWSCredentials
from security_token_service import SecurityTokenService


class AssumeRole(SecurityTokenService):

    def assume_role(self, assume_role_args):
        response = self.client.assume_role(RoleArn=assume_role_args.role_arn,
                                           RoleSessionName=assume_role_args.role_session_name)

        response_credentials = response['Credentials']
        aws_credentials = AWSCredentials(access_key_id=response_credentials['AccessKeyId'],
                                         secret_access_key=response_credentials['SecretAccessKey'],
                                         session_token=response_credentials['SessionToken'],
                                         expiration=response_credentials['Expiration'])

        return aws_credentials
