# Created by tonimaxx at 1/5/22
Feature: Verify if the test works

  Scenario: Verify Google I am feeling button works correctly
    Given User is at Google Homepage
    When User clicks on I am feeling button
    Then A page is shown, no 404 error

  Scenario: Verify Gettop Homepage Top Menus
    Given User is at Gettop Homepage
    Then Element Gettop Homepage Logo|Gettop Footer Copyright|Cart Logo|Latest Product|Top Menu Mac is existed
    Then User clicks on Top Menu Mac
    Then Element Bread Crumb is existed
    And Element Bread Crumb contains text MACBOOK
    Then Hover mouse on Top Menu Mac3
    Then Element Left Menu contains 6 elements

  Scenario Outline: Verify Search Feature
    Given User is at Gettop Homepage
    Then Hover mouse on Search Icon
    And Type <search> to Search Field and Enter
    Then Element Bread Crumb contains text <expect>
    Examples:
    | search      | expect      |
    | MAC         | MAC         |
    | IPHONE      | IPHONE      |
    | IPAD        | IPAD        |
    | WATCH       | WATCH       |
    | ACCESSORIES | ACCESSORIES |