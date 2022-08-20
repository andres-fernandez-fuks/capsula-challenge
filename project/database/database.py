from project.models.account import Account


class Database:
    """
    Mockea la base de datos, solamente almacena las Accounts en memoria, en un diccionario
    """

    def __init__(self):
        self.accounts = {}

    def get_by_id(self, id):
        if id not in self.accounts:
            self.accounts[id] = Account(
                id
            )  # debería lanzar error, pero es más fácil en este ejercicio que no lo haga
        return self.accounts[id]

