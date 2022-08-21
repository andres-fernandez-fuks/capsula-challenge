from flask import Flask
from project.database.database import Database

db = Database()

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from project.controllers.account_controller import account_controller
    from project.controllers.transaction_controller import transaction_controller
    from project.controllers.database_controller import database_controller

    app.register_blueprint(account_controller)
    app.register_blueprint(transaction_controller)
    app.register_blueprint(database_controller)
