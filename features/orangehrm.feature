Feature: orangeHRM logo
  Scenario: logo is presence in orangeHRM home page
    Given  launch chrome browser
    When  open orangehrm homepage
    Then  verify that the logo present on page
    And  close browser