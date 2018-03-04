from data_models import AssumeRoleArgs, AssumedRoleUser, Credentials, AssumedRoleResponse
from security_token_service import SecurityTokenService
from typing import Any, Dict


class AssumeRole(SecurityTokenService):

    def assume_role(self, assume_role_args: AssumeRoleArgs):
        response = self.client.assume_role(RoleArn=assume_role_args.role_arn,
                                           RoleSessionName=assume_role_args.role_session_name)

        response_credentials: Dict[str, Any] = response['Credentials']
        credentials: Credentials = Credentials(access_key_id=response_credentials['AccessKeyId'],
                                               secret_access_key=response_credentials['SecretAccessKey'],
                                               session_token=response_credentials['SessionToken'],
                                               expiration=response_credentials['Expiration'])

        return credentials
