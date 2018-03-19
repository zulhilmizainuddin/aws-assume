from datetime import datetime

from assume_role_executor import AssumeRoleExecutor
from assumed_role_response_cache import AssumedRoleResponseCache
from data_models import AssumedRoleResponse, AssumedRoleResponseCredentials, Credentials
from security_token_service import SecurityTokenService


class AssumeRoleCacheExecutor(AssumeRoleExecutor):

    def __init__(self, role_arn: str, role_session_name: str, security_token_service: SecurityTokenService) -> None:
        self.role_arn = role_arn
        self.role_session_name = role_session_name
        self. security_token_service = security_token_service

        self.response_cache = AssumedRoleResponseCache()

    def execute(self) -> Credentials:
        credentials: Credentials = None

        assumed_role_response: AssumedRoleResponse = self.response_cache.get_response_from_cache(self.role_arn, self.role_session_name)
        if assumed_role_response is not None:

            expiration: datetime = assumed_role_response['Credentials']['Expiration']
            if expiration is not None and datetime.now() < expiration:
                credentials = self.compose_credentials(assumed_role_response)
            else:
                assumed_role_response = self.newly_request_and_cache_assume_role()
                credentials = self.compose_credentials(assumed_role_response)
        else:
            assumed_role_response = self.newly_request_and_cache_assume_role()
            credentials = self.compose_credentials(assumed_role_response)

        return credentials

    def newly_request_and_cache_assume_role(self) -> AssumedRoleResponse:
        assumed_role_response: AssumedRoleResponse = self.security_token_service.assume_role()

        self.response_cache.set_response_to_cache(self.role_arn, self.role_session_name, assumed_role_response)

        return assumed_role_response

    def compose_credentials(self, assumed_role_response: AssumedRoleResponse) -> Credentials:
        response_credentials: AssumedRoleResponseCredentials = assumed_role_response['Credentials']

        credentials = Credentials(access_key_id=response_credentials['AccessKeyId'],
                                  secret_access_key=response_credentials['SecretAccessKey'],
                                  session_token=response_credentials['SessionToken'],
                                  expiration=response_credentials['Expiration'])

        return credentials
