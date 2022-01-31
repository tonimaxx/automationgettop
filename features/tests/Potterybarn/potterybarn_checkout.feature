# Created by Jarus Soontornsing
Feature: Test Scenario for Potterybarn Website

#  Background: Precondition for all tests

  Scenario: Verify adding products to cart
    Given User is at Potterybarn.com
    When Potterbarn Homepage is loaded
    And Search for sectional from Potterybarn homepage
    And Click on a product at column 2 row 3
    And Add current product to cart
    And Search for pillow from Potterybarn homepage
    And Click on a product at column 1 row 1
    And Add current product to cart
    And Continue to Checkout
    And Place an order without Address information
    And Place an order without Email
    And Place an order without Payment information
    Then All errors are thrown as expected