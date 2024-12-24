from src.models.interfaces.user_repository import UserRepositoryInterface
from .interfaces.balance_editor_controller import BalanceEditorControllerInterface

class BalanceEditorController(BalanceEditorControllerInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def edit(self, user_id: int, new_balance: float) -> dict:
        self.__user_repository.edit_balance(user_id, new_balance)
        formated_response = self.__format_response(new_balance)

        return formated_response
        
    def __format_response(self, new_balance: float) -> dict:
        return {
            "type": "User",
            "count": 1,
            "new balance": new_balance
        }
        