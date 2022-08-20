from project.models.account import Account

class AccountRepository:
    '''
    Mockea un controlador de cuentas, que debería interactuar con la base de datos
    '''
    def get_by_id(self, account_id):
        '''
        Retorna una cuenta por su id
        '''
        return Account(account_id)
    def get_balance(self, account_id):
        '''
        Retorna el saldo de una cuenta
        '''
        return Account(account_id).get_balance()
    def handle_transaction(self, account_id, transaction):
        '''
        Procesa una transacción
        '''
        Account(account_id).
    '''