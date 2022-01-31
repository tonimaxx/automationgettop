# Created by Jarus Soontornsing
Feature: Test Scenarios for Currency API


  Background: User has authorized already
    Given I am an authorized user


  Scenario: Verify correct HTTP 200 status code
    When I test all Endpoints
    Then All Endpoints return valid


  Scenario: Verify if currency count is correct
    When I get all currencies
    Then There are 182 currencies listed


  Scenario Outline: Verify Get the currency list with base currency
  When I get currency with <basecurrency> as base currency
  Then Base currency result is valid
  Examples:
  | basecurrency  |
  | eur           |
  | usd           |
  | thx           |
  | sgd           |
  | eth           |


  Scenario Outline: Get the currency value
  When I get currency of <basecurrency> in <resultcurrency>
  Then I got result currency of <resultcurrency>
  Examples:
  | basecurrency  | resultcurrency |
  | eur           | jpy            |
  | eur           | xyz            |
  | eur           | usd            |
  | usd           | eur            |
  | thb           | usd            |
  | sgd           | jpy            |
  | eth           | usd            |


#  Others to test
#  Scenario: Verify Schema
#  Scenario: Verify Response payload
#  Scenario: Verify Positive Tests
#  Scenario: Verify Negative Tests
#  Scenario: Verify Destructive Tests
#  Scenario: Load Tests
#  Scenario: Stress Tests
#  Scenario: Performance Tests
#  Scenario: Usability Tests