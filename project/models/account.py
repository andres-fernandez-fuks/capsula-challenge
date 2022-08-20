from project.exceptions.insufficient_funds_exception import InsufficientFundsException
from project.models.transaction import Transaction, TransactionType


class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException()
        self.balance -= amount

    def handle_transaction(self, transaction: Transaction):
        if transaction.transaction_type == TransactionType.INCOME:
            self.deposit(transaction.amount)
        elif transaction.transaction_type == TransactionType.EXPENDITURE:
            self.withdraw(transaction.amount)

    def get_id(self):
        return self.id

    def get_balance(self):
        return self.balance

