from project.models.transaction import Transaction, TransactionType

def test_income_transaction_creation():
    '''
    Prueba la creación de una transacción de ingreso de dinero
    '''
    transaction = Transaction(1, TransactionType.INCOME, 100)
    assert transaction.account_id == 1
    assert transaction.transaction_type == TransactionType.INCOME
    assert transaction.amount == 100

def test_expenditure_transaction_creation():
    '''
    Prueba la creación de una transacción de egreso de dinero
    '''
    transaction = Transaction(1, TransactionType.EXPENDITURE, 100)
    assert transaction.account_id == 1
    assert transaction.transaction_type == TransactionType.EXPENDITURE
    assert transaction.amount == 100