from botocore.exceptions import ClientError
from data_models import AssumeRoleArgs, AssumedRoleUser, Credentials, AssumedRoleResponse
from security_token_service import SecurityTokenService
from typing import Any, Dict


class AssumeRole(SecurityTokenService):

    def assume_role(self, assume_role_args: AssumeRoleArgs) -> AssumedRoleResponse:
        try:
            response: Dict[str, Any] = self.client.assume_role(RoleArn=assume_role_args.role_arn,
                                                               RoleSessionName=assume_role_args.role_session_name)
        except ClientError:
            raise
        else:
            response_assumed_role_user: Dict[str, str] = response['AssumedRoleUser']
            assumed_role_user = AssumedRoleUser(assumed_role_id=response_assumed_role_user['AssumedRoleId'],
                                                arn=response_assumed_role_user['Arn'])

            response_credentials: Dict[str, Any] = response['Credentials']
            credentials = Credentials(access_key_id=response_credentials['AccessKeyId'],
                                      secret_access_key=response_credentials['SecretAccessKey'],
                                      session_token=response_credentials['SessionToken'],
                                      expiration=response_credentials['Expiration'])

            assumed_role_response = AssumedRoleResponse(assumed_role_user=assumed_role_user,
                                                        credentials=credentials)

            return assumed_role_response
