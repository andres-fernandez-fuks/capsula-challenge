class InsufficientFundsException(Exception):
    def __init__(self):
        self.message = "Saldo insuficiente"