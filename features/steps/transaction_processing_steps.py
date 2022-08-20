from behave import given, when, then, step
from project.models.account import Account
import requests


POST_URL = "http://localhost:8080/transactions"


def get_balance_url(account_id):
    return f"http://localhost:8080/accounts/{account_id}/balance"


@given("I have a new account with id {account_id:d}")
def step_impl(context, account_id):
    context.account_id = account_id


@when(
    "an {transaction_type} transaction is created to my account with a value of {transaction_amount:d}"
)
def step_impl(context, transaction_type, transaction_amount):
    request_data = {
        "transaction_type": transaction_type,
        "amount": transaction_amount,
        "account_id": context.account_id,
    }
    request = requests.post(POST_URL, json=request_data)
    context.request_status = request.status_code


@then("the balance of my account should be {expected_balance:d}")
def step_impl(context, expected_balance):
    request = requests.get(get_balance_url(context.account_id))
    balance = request.json()["balance"]
    assert balance == expected_balance


@given("my account with id {account_id:d} has a balance of {balance:d}")
def step_impl(context, account_id, balance):
    context.account_id = account_id
    request_data = {
    "transaction_type": "income",
    "amount": balance,
    "account_id": account_id,
    }
    request = requests.post(POST_URL, json=request_data)


@then("an error should be raised")
def step_impl(context):
    assert context.request_status != 200
