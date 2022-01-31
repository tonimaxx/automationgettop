# Created by Toni Jarus Soontornsing at 11/27/21
Feature: Test Scenario for verifying Categories functionality


  Scenario: User sees correct categories under Browse
    Given Open Home Page
    Then Verify all correct categories ACCESSORIES|MACBOOK|IPAD|IPHONE are under Browse


  Scenario: User click on categories under Browse and correct page opens
    Given Open Home Page
    Then Verify click on categories ACCESSORIES|MACBOOK|IPAD|IPHONE and correct page opens