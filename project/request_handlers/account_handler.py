from tornado import web
from project.repositories.account_repository import AccountRepository


class AccountHandler(web.RequestHandler):
    def get(self, account_id):
        account = AccountRepository.get_by_id(account_id)
        return account.get_balance()
