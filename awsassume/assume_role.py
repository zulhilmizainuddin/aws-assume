from botocore.exceptions import ClientError
from data_models import AssumeRoleArgs, Credentials
from security_token_service import SecurityTokenService
from typing import Any, Dict


class AssumeRole(SecurityTokenService):

    def __init__(self, assume_role_args: AssumeRoleArgs):
        super().__init__()

        self.assume_role_args: AssumeRoleArgs = assume_role_args

    def assume_role(self) -> Credentials:
        try:
            response: Dict[str, Any] = self.client.assume_role(RoleArn=self.assume_role_args.role_arn,
                                                               RoleSessionName=self.assume_role_args.role_session_name)
        except ClientError:
            raise
        else:
            response_credentials: Dict[str, Any] = response['Credentials']
            credentials = Credentials(access_key_id=response_credentials['AccessKeyId'],
                                      secret_access_key=response_credentials['SecretAccessKey'],
                                      session_token=response_credentials['SessionToken'],
                                      expiration=response_credentials['Expiration'])

            return credentials
