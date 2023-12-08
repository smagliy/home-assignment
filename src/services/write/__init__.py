from abc import ABC, abstractmethod


class WriteService(ABC):
    @abstractmethod
    def write(self):
        pass
