# Created by tonimaxx at 11/26/21
Feature: Test Scenario for Basic functionality


  Scenario: Verify user can see Home Page
    Given Open Home Page
    Then Home Page is shown


  Scenario: User can open the home page
    Given Open Category ipad
    Then Home Page is shown


  Scenario: Verify all top menu product urls are not #
    Given Open Home Page
    Then Expected all products url are not #


  Scenario: User sees correct categories under Browse
    Given Open Home Page
    Then All categories are displayed correctly


  Scenario: User click on categories under Browse and correct page opens
    Given Open Home Page
    Then Home Page is shown
    Then All browse menu items are displayed correctly



