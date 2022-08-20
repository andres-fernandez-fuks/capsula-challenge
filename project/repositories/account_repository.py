from project.models.account import Account


class AccountRepository:
    """
    Mockea un controlador de cuentas, que debería interactuar con la base de datos
    """

    @classmethod
    def get_by_id(cls, account_id):
        """
        Retorna una cuenta por su id
        """
        return Account(account_id)
