import boto3

from abc import ABCMeta, abstractmethod
from data_models import Credentials


class SecurityTokenService(object):
    __metaclass__ = ABCMeta

    def __init__(self) -> None:
        self.client = boto3.client('sts')

    @abstractmethod
    def assume_role(self) -> Credentials:
        pass
