# Created by Toni Jarus Soontornsing
Feature: Test Scenario for ...

  
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