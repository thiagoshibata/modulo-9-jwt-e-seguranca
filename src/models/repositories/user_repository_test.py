from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from unittest.mock import Mock

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_registry_user():
    username = "fred"
    password = "12345"
    balance = 0


    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, balance)
    
def test_edit_balance():
    user_id = 123
    balance = 100.00

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.edit_balance(user_id,balance)

    cursor = mock_connection.cursor.return_value

    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (balance, user_id)

    mock_connection.commit.assert_called_once()

def test_get_user_by_username():
    username = "meuUserName"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user_by_username(username)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)

    cursor.fetchone.assert_called_once()

""" def test_user_repository():
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
    print(user2)  """
    