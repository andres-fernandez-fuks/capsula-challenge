from project.models.account import Account
from project import db


class AccountRepository:
    """
    Mockea un controlador de cuentas, que "interactua" con la base de datos
    """

    @classmethod
    def get_by_id(self, id):
        return db.get_by_id(id)
