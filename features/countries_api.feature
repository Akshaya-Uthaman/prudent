Feature: Countries functionality

  Scenario: Test get countries api
    Given The user hits the get countries with valid data
    Then The user hits the get countries with invalid auth
    