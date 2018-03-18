from assume_role_executor import AssumeRoleExecutor
from data_models import Credentials
from security_token_service import SecurityTokenService


class AssumeRoleNoCacheExecutor(AssumeRoleExecutor):

    def __init__(self, security_token_service: SecurityTokenService) -> None:
        self.security_token_service = security_token_service

    def execute(self) -> Credentials:
        return self.security_token_service.assume_role()
