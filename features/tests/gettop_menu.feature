# Created by Toni Jarus Soontornsing at 12/1/21
Feature: Test Scenario for Gettop Menu functionality


  Scenario Outline: Verify user can hover a menu and see correct menu options
    Given Open Home Page
    When Hover over top menu <topmenu>
    Then Menu option appear with expected keyword <keyword>
    Examples:
    | topmenu     | keyword     |
    | MAC         | MacBook     |
    | IPHONE      | iPhone      |
    | IPAD        | iPad        |
    | WATCH       | Watch       |
    | ACCESSORIES | Cases       |


  Scenario Outline: Verify user can select product from top menu and correct page is opened
    Given Open Home Page
    When Click top menu <topmenu>
    Then The correct page is opened with expected keyword <keyword>
    Examples:
    | topmenu     | keyword     |
    | MAC         | MacBook     |
    | IPHONE      | iPhone      |
    | IPAD        | iPad        |
    | WATCH       | Watch       |
    | ACCESSORIES | Accessories |