from abc import ABC, abstractmethod

class LoginCreatorControllerInterface(ABC):

    @abstractmethod
    def creat(self, username: str, password: str) -> dict:
        pass