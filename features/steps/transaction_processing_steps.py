from behave import given, when, then, step
from project.models.account import Account
import requests
from http import HTTPStatus


ACCOUNT_ID = 1
POST_TRANSACTION_URL = "http://localhost:8080/transactions"
GET_BALANCE_URL = f"http://localhost:8080/accounts/{ACCOUNT_ID}/balance"


@when(
    "an {transaction_type} transaction is created to my account with a value of {transaction_amount:d}"
)
def step_impl(context, transaction_type, transaction_amount):
    request_data = {
        "transaction_type": transaction_type,
        "amount": transaction_amount,
        "account_id": ACCOUNT_ID,
    }
    request = requests.post(POST_TRANSACTION_URL, json=request_data)
    context.request_status = request.status_code


@then("the balance of my account should be {expected_balance:d}")
def step_impl(context, expected_balance):
    request = requests.get(GET_BALANCE_URL)
    balance = request.json()["balance"]
    assert balance == expected_balance


@given("my account has a balance of {balance:d}")
def step_impl(context, balance):
    request_data = {
    "transaction_type": "income",
    "amount": balance,
    "account_id": ACCOUNT_ID,
    }
    request = requests.post(POST_TRANSACTION_URL, json=request_data)


@then("an error should be raised")
def step_impl(context):
    assert context.request_status == HTTPStatus.UNPROCESSABLE_ENTITY
