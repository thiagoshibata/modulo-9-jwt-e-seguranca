from abc import ABC, abstractmethod

class BalanceEditorControllerInterface(ABC):
    def edit(self, user_id: int, new_balance: float) -> dict:
        pass
