from abc import ABC, abstractmethod
from data_models import Credentials


class AssumeRoleExecutor(ABC):

    @abstractmethod
    def execute(self) -> Credentials:
        pass
