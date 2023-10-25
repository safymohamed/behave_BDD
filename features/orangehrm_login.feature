 Feature: orangehrm login

   Scenario: login to orangehrm with valid parameters
     Given I launch chrome browser
     When  I open orangehrm webpage
     And   I enter username "Admin" and password "admin123"
     And   I press the "login" button
     Then  User can enter to dashboard page

   Scenario Outline: : login to orangehrm with invalid parameters
     Given I launch chrome browser
     When  I open orangehrm webpage
     And   I enter username "<username>" and password "<password>"
     And   I press the "login" button
     Then  User can enter to dashboard page
     Examples:
      | username | password |
      | Admin    | admin123 |
      | admin123 | Admin    |
      | adminxzm | Admin    |
      | Admin    | adminxzm |