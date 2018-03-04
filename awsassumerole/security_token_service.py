import boto3

from abc import ABCMeta, abstractmethod
from data_models import AssumeRoleArgs, AssumedRoleResponse


class SecurityTokenService(object):
    __metaclass__ = ABCMeta

    def __init__(self) -> None:
        self.client = boto3.client('sts')

    @abstractmethod
    def assume_role(self, assume_role_args: AssumeRoleArgs) -> AssumedRoleResponse:
        pass
