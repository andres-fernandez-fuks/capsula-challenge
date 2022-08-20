from flask import Blueprint, jsonify, request
from project.repositories.account_repository import AccountRepository

ACCOUNT_ENDPOINT = "/accounts"
account_controller = Blueprint("account_controller", __name__)

@account_controller.route(f"{ACCOUNT_ENDPOINT}/<account_id>/balance", methods=["GET"])
def get_account_balance(account_id):
    account_id = int(account_id)
    account = AccountRepository.get_by_id(account_id)
    return jsonify({"balance": account.get_balance()})
