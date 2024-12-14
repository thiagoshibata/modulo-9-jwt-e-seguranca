from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler

class UserRegister:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
        self.__passoword_handle = PasswordHandler()
    
    def registry(self, username: str, password: str) -> dict:
        hashed_password = self.__create_hashed_password(password)
        self.__registry_new_user(username, hashed_password)
        return self.__format_response(username)

    def __create_hashed_password(self, password: str) -> str:
        hashed_passowrd = self.__passoword_handle.encrypt_password(password)
        return hashed_passowrd
    
    def __registry_new_user(self, username: str, hashed_passowrd: str) -> None:
        self.__user_repository.registry_user(username, hashed_passowrd)

    def __format_response(self, username: str) -> dict:
        return {
            "type": "User",
            "count": 1,
            "username": username
        }
    