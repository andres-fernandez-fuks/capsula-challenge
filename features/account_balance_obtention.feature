Feature: Account balance obtention
    Scenario: Getting the balance of the account
        Given I have an account with id 1
        When I get the balance of the account
        Then I should get 0
    
