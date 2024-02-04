Feature: Search functionality

  Scenario: Test search by filters api
    Given The user hits the search api with valid data
    Then The user hits the search api with invalid auth
    Then The user hits the search api without country key