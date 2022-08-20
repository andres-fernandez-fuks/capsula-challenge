from tornado import web
from project.helpers.transaction_parser import TransactionParser
from project.repositories.account_repository import AccountRepository


class TransactionHandler(web.RequestHandler):
    def post(self):
        try:
            account_id = self.get_body_argument("account_id")
            transaction_data = self.get_body_argument("transaction")
            account = AccountRepository.get_by_id(account_id)
            transaction = TransactionParser.parse(transaction_data)
            account.handle_transaction(transaction)
            return "OK"
        except Exception as e:
            return e.message

