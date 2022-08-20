from project.exceptions.invalid_input_exception import InvalidInputException
from project.models.transaction import Transaction, TransactionType


class TransactionParser:
    """
    Clase encargada de crear una transacción a partir de los datos recibidos.
    Está creada con el objetivo de mantener la arquitectura hexagonal del proyecto, y que no sea la clase
    Transaction (propia del modelo) quien deba conocer el formato de los datos recibidos.
    """

    TRANSACTION_INPUT_TYPE_INCOME = "income"
    TRANSACTION_INPUT_TYPE_EXPENDITURE = "expenditure"

    @classmethod
    def parse(cls, transaction_data):
        try:
            transaction_type = cls.determine_transaction_type(
                transaction_data["transaction_type"]
            )
            amount = transaction_data["amount"]
            account_id = transaction_data["account_id"]
            return Transaction(
                transaction_type=transaction_type, amount=amount, account_id=account_id
            )
        except ValueError as e:
            raise InvalidInputException("saldo")

    @classmethod
    def determine_transaction_type(cls, transaction_input_type):
        if transaction_input_type == cls.TRANSACTION_INPUT_TYPE_INCOME:
            return TransactionType.INCOME
        elif transaction_input_type == cls.TRANSACTION_INPUT_TYPE_EXPENDITURE:
            return TransactionType.EXPENDITURE
        else:
            raise InvalidInputException("tipo de transacción")
