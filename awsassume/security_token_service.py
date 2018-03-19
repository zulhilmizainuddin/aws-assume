import boto3

from abc import ABC, abstractmethod
from data_models import AssumedRoleResponse


class SecurityTokenService(ABC):

    def __init__(self) -> None:
        self.client = boto3.client('sts')

    @abstractmethod
    def assume_role(self) -> AssumedRoleResponse:
        pass
