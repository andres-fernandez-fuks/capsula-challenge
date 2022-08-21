class InsufficientFundsException(Exception):
    def __str__(self):
        return "Saldo insuficiente para realizar la transacción"