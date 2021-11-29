# Created by Toni Jarus Soontornsing at 11/27/21
Feature: Test Scenario for verifying Categories functionality


  Scenario: User sees correct categories under Browse
    Given Open Home Page
    Then All categories are displayed correctly


  Scenario: User click on categories under Browse and correct page opens
    Given Open Home Page
    Then Home Page is shown
    Then All browse menu items are displayed correctly
