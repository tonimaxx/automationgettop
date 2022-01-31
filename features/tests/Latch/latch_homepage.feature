# Created by tonimaxx at 1/17/22
Feature: Test Scenario for Latch Homepage
  # Enter feature description here

  Background: Precondition for all tests
    Given User is at Latch.com

#  Scenario: Verify top menus LatchOS navigate correctly (Auto)
#    Given User is at Latch.com
#    When Page is ready with Latch Heading Word existed
#    Then Click all LatchOS sub menus and no broken link

  Scenario Outline: Verify top menus LatchOS navigate correctly
#    Given User is at Latch.com
    When Page is ready with Latch Heading Word existed
    Then Click LatchOS sub menu <submenu> and navigate correctly
    Examples:
    | submenu                       |
    | Smart Access                  |
    | Guest and Delivery Management |
    | Smart Home and Sensors        |
    | Connectivity                  |
    | Personalization and Services  |


