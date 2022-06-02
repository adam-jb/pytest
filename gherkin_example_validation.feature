Feature: Phone number validation application

    Scenario: validate a number
        Given I have a number +311234555
        When I run number validation application
        Then Number is normalized 
        And Cache is checked for presence of this number
        And External API is called if cache doesn't contains the number 
