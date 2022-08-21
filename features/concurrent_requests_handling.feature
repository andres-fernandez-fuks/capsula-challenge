Feature: Concurrent requests handling
    Scenario: Processing concurrent transaction creations and balance obtentions
        Given multiple transactions with values 30, 60, 100 enter my account
        When the transactions are processed and I check my account's balance
        Then all the balances obtained are valid