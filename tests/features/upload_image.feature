Feature: Upload an image for a pet

  Scenario Outline: Successfully upload an image for a pet
    Given the pet ID is <pet_id>
    And the metadata is "<metadata>"
    And the image path is "<image_path>"
    When I upload the image
    Then the response status code should be <status_code>
    And the response code should be <response_code>

  Examples:
    | pet_id | metadata                 | image_path             | status_code | response_code |
    | 203    | Some additional metadata | F:/AutomationTest_Project/SeleniumWebDriver_AutomationTest/petStore/tests/utils/Dog.jpg   | 200         | 200           |
