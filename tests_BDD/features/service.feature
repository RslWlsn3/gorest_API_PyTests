Feature: Simple GET request
  As a user I want to be able to connect and perform a GET request


  Scenario: Perform GET request
    Given GET request is performed on the gorest API    
    Then the response status code is "200"