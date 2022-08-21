import threading
from project.exceptions.insufficient_funds_exception import InsufficientFundsException
from project.models.transaction import Transaction, TransactionType


class Account:
    """
    Representa una cuenta, con un identificador y un saldo. Maneja transacciones de ingreso y egreso.
    """
    def __init__(self, id, starting_balance=0):
        self.id = id
        self.balance = starting_balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException()
        self.balance -= amount

    def handle_transaction(self, transaction: Transaction):
        with self.lock:
            if transaction.transaction_type == TransactionType.INCOME:
                self.deposit(transaction.amount)
            elif transaction.transaction_type == TransactionType.EXPENDITURE:
                self.withdraw(transaction.amount)

    def get_id(self):
        return self.id

    def get_balance(self):
        with self.lock:
            return self.balance

