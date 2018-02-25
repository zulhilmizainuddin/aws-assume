from abc import ABCMeta, abstractmethod
import boto3


class SecurityTokenService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.client = boto3.client('sts')

    @abstractmethod
    def assume_role(self, assume_role_args): pass
