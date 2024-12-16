from src.drivers.password_handler import PasswordHandler
from .login_creator_controller import LoginCreatorController

username = "meuUserName"
password = "minhaSenha"
hashed_password = PasswordHandler().encrypt_password(password)

class MockUserRepository:
    def get_user_by_username(self, username):
        return (10, username, hashed_password)

def test_create():
    login_creator = LoginCreatorController(MockUserRepository())
    response = login_creator.creat(username, password)

    print()
    print(response)

    assert response["access"] == True
    assert response["username"] == username
    assert response["token"] is not None