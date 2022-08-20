from behave import given, when, then, step
from project.repositories.account_repository import AccountRepository


@given("I have an account with id {account_id:d}")
def step_impl(context, account_id):
    context.account = AccountRepository.get_by_id(account_id)


@when("I get the balance of the account")
def step_impl(context):
    context.balance = context.account.get_balance()


@then("I should get {expected_value:d}")
def step_impl(context, expected_value):
    assert context.balance == expected_value
