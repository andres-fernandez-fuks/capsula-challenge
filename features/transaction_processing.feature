Feature: Transaction processing
    Background:
        Given I have a new account with id 1
    Scenario: Processing an income transaction
        When an income transaction is created to my account with a value of 100
        Then the balance of my account should be 100
