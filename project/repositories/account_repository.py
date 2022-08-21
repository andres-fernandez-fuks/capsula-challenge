from project.models.account import Account
from project import db


class AccountRepository:
    """
    Mockea un controlador de cuentas, que "interactua" con la base de datos
    """

    @staticmethod
    def get_by_id(id):
        return db.get_by_id(id)

    @staticmethod
    def reset_database():
        db.reset()
