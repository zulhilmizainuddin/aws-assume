import boto3

from abc import ABC, abstractmethod
from data_models import AssumedRoleResponse


class SecurityTokenService(ABC):

    def __init__(self, region: str = None) -> None:
        self.client = boto3.client('sts', region_name=region)

    @abstractmethod
    def assume_role(self) -> AssumedRoleResponse:
        pass
