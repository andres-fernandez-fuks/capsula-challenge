import pytest
from project.exceptions.insufficient_funds_exception import InsufficientFundsException
from project.models.account import Account
from project.models.transaction import Transaction, TransactionType


def test_account_creation():
    """
    Prueba la creación de una cuenta
    """
    account = Account(1)
    assert account.get_id() == 1
    assert account.get_balance() == 0


def test_account_deposit():
    """
    Prueba el depósito (transacción de ingreso) de una cuenta
    """
    account = Account(1)
    income_transaction = Transaction(1, TransactionType.INCOME, 100)
    account.handle_transaction(income_transaction)
    assert account.get_balance() == 100


def test_correct_account_withdrawal():
    """
    Prueba el retiro (transacción de egreso) de una cuenta
    """
    account = Account(1)
    income_transaction = Transaction(1, TransactionType.INCOME, 100)
    account.handle_transaction(income_transaction)
    expenditure_transaction = Transaction(1, TransactionType.EXPENDITURE, 50)
    account.handle_transaction(expenditure_transaction)
    assert account.get_balance() == 50


def test_insufficient_funds_withdrawal_raises_exception():
    """
    Prueba que el retiro de una cuenta con saldo insuficiente lance la excepción adecuada
    """
    account = Account(1)
    expenditure_transaction = Transaction(1, TransactionType.EXPENDITURE, 50)
    with pytest.raises(InsufficientFundsException):
        account.handle_transaction(expenditure_transaction)
    assert True  # solamente pruebo que lance la excepción


def test_insufficient_funds_withdrawal_does_not_modify_account_balance():
    """
    Prueba que el retiro de una cuenta con saldo insuficiente no modifique el saldo de la cuenta
    """
    account = Account(1)
    expenditure_transaction = Transaction(1, TransactionType.EXPENDITURE, 50)
    with pytest.raises(InsufficientFundsException):
        account.handle_transaction(expenditure_transaction)
    assert account.get_balance() == 0
