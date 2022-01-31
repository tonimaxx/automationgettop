# Created by tonimaxx at 1/5/22
Feature: Verify if user can login successfully GMAIL
  # Enter feature description here

  Scenario: # Log in to Gmail
    Given I am at Gmail main page
    When User fill credentials
    And Click the submit button
    Then User are logged in
