from flask import Blueprint, jsonify, request
from project.helpers.transaction_parser import TransactionParser
from project.repositories.account_repository import AccountRepository
from project.helpers.exception_handler import ExceptionHandler

TRANSACTIONS_ENDPOINT = "/transactions"
transaction_controller = Blueprint("transaction_controller", __name__)

@transaction_controller.route(f"{TRANSACTIONS_ENDPOINT}", methods=["POST"])
def handle_transaction():
    try:
        transaction_data = request.get_json()
        transaction = TransactionParser.parse(transaction_data)
        account = AccountRepository.get_by_id(transaction.get_account_id())
        account.handle_transaction(transaction)
        return jsonify({"balance": account.get_balance()})
    except Exception as e:
        return ExceptionHandler.handle_exception(e)

      

