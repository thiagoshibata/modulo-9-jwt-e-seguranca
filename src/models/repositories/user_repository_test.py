from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository

def test_user_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    username = "thiagoshibata2"
    password = "123456"

    repo.registry_user(username, password)
    user = repo.get_user_by_username(username)
    print()
    print(user)

    user_id = user[0]
    new_balance = 1350.00
    repo.edit_balance(user_id, new_balance)
    user2 = repo.get_user_by_username(username)
    print()
    print(user2) 

    