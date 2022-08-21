from flask import Blueprint, jsonify, request
from project.repositories.account_repository import AccountRepository

DATABASE_ENDPOINT = "/database"
database_controller = Blueprint("database_controller", __name__)

@database_controller.route(f"{DATABASE_ENDPOINT}/reset", methods=["POST"])
def reset_database():
    '''
    Endpoint usado para resetear la base de datos, solamente usado para pruebas.
    '''
    AccountRepository.reset_database()
    return jsonify({"message": "Database reset"})
