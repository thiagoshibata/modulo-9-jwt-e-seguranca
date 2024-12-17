from src.models.interfaces.user_repository import UserRepositoryInterface

class BalanceEditor:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def edit(self, user_id: int, new_balance: float) -> dict:
        self.__user_repository.edit_balance(user_id, new_balance)
        self.__format_response(new_balance)

    def __format_response(new_balance: float) -> dict:
        return {
            "type": "User",
            "count": 1,
            "new balance": new_balance
        }