# Created by Toni Jarus Soontornsing
Feature: Test Scenario for ...

  Scenario: Python Homepage
    Given User is at Python.org
    When Page is ready with Python Homepage Logo existed
    Then Click all elements in Python Homepage Main Navigator and no broken link
    Then Click all elements in Python Homepage Slide Menu Buttons and no broken link


  Scenario: Verify Homepage
    Given User is at Gettop Homepage


  Scenario Outline: Verify Search Feature
    Given User is at Gettop Homepage
    Then Hover mouse on Search Icon
    And Type <search> to Search Field and Enter
    Then Element Bread Crumb contains text <expect>
    Examples:
    | search      | expect      |
    | MAC         | MAC         |
    | IPHONE      | IPHONE      |
#    | IPAD        | IPAD        |
#    | WATCH       | WATCH       |
#    | ACCESSORIES | ACCESSORIES |