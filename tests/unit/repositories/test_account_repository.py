from project.repositories.account_repository import AccountRepository
from project.models.transaction import Transaction, TransactionType

def test_account_obtention():
    '''
    Prueba la obtención de una cuenta
    '''
    account = AccountRepository.get_by_id(1)
    assert account.id == 1
    assert account.balance == 0

def test_account_deposit():
    '''
    Prueba que la modificación de una cuenta queda actualizada en la "base de datos"
    '''
    account = AccountRepository.get_by_id(1)
    income_transaction = Transaction(1, TransactionType.INCOME, 100)
    account.handle_transaction(income_transaction)
    assert AccountRepository.get_by_id(1).balance == 100