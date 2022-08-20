from enum import Enum
class TransactionType(Enum):
    INCOME = 1
    EXPENDITURE = 2

class Transaction:
    def __init__(self, account_id: int, transaction_type: TransactionType, amount: float):
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount

    def get_account_id(self):
        return self.account_id