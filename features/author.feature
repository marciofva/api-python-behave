@author
Feature: Author

  Scenario Outline: Author request should be created
    Given this author template "<request_template>"
    When I send create author request
    Then I receive status code equals to "<expected_status_code>"

    Examples: Author requests
      | request_template          | expected_status_code   |
      | valid                     | 200                    |
      | invalid_idBook            | 400                    |


  Scenario: Author request should be retrieved
    Given the author id "5"
    When I send retrieve author request
    Then I receive status code equals to "200"
