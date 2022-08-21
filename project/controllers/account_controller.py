from flask import Blueprint, jsonify, request
from project.helpers.exception_handler import ExceptionHandler
from project.repositories.account_repository import AccountRepository

ACCOUNT_ENDPOINT = "/accounts"
account_controller = Blueprint("account_controller", __name__)
"""
Controlador encargado de manejar todas las requests asociadas a las cuentas (Accounts).
"""


@account_controller.route(f"{ACCOUNT_ENDPOINT}/<account_id>/balance", methods=["GET"])
def get_account_balance(account_id):
    try:
        account_id = int(account_id)
        account = AccountRepository.get_by_id(account_id)
        return jsonify({"balance": account.get_balance()})
    except Exception as e:
        return ExceptionHandler.handle_exception(e)
