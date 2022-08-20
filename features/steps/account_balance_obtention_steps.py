import requests
from behave import given, when, then, step

def get_balance_url(account_id):
    return f"http://localhost:8080/accounts/{account_id}/balance"

@given("I have an account with id {account_id:d}")
def step_impl(context, account_id):
    context.account_id = account_id


@when("I get the balance of the account")
def step_impl(context):
    request = requests.get(get_balance_url(context.account_id))
    context.balance = request.json()["balance"]


@then("I should get {expected_value:d}")
def step_impl(context, expected_value):
    assert context.balance == expected_value
