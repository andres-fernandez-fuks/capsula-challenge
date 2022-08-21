from re import S
from threading import Thread
import time
from behave import given, when, then, step
import requests

ACCOUNT_ID = 1
POST_TRANSACTION_URL = "http://localhost:8080/transactions"

def create_transactions(transaction_amounts):
    for amount in transaction_amounts:
        request_data = {
            "transaction_type": "income",
            "amount": amount,
            "account_id": ACCOUNT_ID,
        }
        request = requests.post(POST_TRANSACTION_URL, json=request_data)

def get_account_status(stop, balances_seen):
    while True:
        request = requests.get(get_balance_url(ACCOUNT_ID))
        balance = request.json()["balance"]
        balances_seen.add(balance)
        if stop():
            break


def get_balance_url(account_id):
    return f"http://localhost:8080/accounts/{account_id}/balance"

@given("multiple transactions with values {t1:d}, {t2:d}, {t3:d} enter my account")
def step_impl(context, t1, t2, t3):
    context.transaction_amounts = [t1, t2, t3]

@when("the transactions are processed and I check my account's balance")
def step_impl(context):
    stop_thread = False
    context.balances_seen = set()
    transaction_creation_thread = Thread(target=create_transactions, args=(context.transaction_amounts,))
    status_obtention_thread = Thread(target=get_account_status, args =(lambda : stop_thread, context.balances_seen))
    transaction_creation_thread.start()
    status_obtention_thread.start()
    time.sleep(3)
    stop_thread = True
    transaction_creation_thread.join()
    status_obtention_thread.join()

@then("all the balances obtained are valid")
def step_impl(context):
    t1, t2, t3 = context.transaction_amounts
    VALID_BALANCES = [0, t1, t1 + t2, t1 + t2 + t3]
    for balance in context.balances_seen:
        assert balance in VALID_BALANCES
