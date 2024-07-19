import unittest
import os
import json
from random import choice, sample
from src.controllers.pet_controller import PetController

class TestFindPetByStatus(unittest.TestCase):
    def setUp(self):
        # Update the path to match the correct location of dataTest.json
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_find_pet_by_status_single_random_status(self):
        status = choice(self.data['status'])
        print(status)
        response = PetController.findPetByStatus(status)
        # Print the response details for debugging. To do so, please uncomment lines 19 and 20 in code.
        # jsonData = response.json()
        # print(json.dumps(jsonData, indent=4, sort_keys=True))
        self.assertEqual(response.status_code, 200, 'Expected status code 200 for findPetByStatus')

    def test_find_pet_by_status_single_available_status(self):
        status = self.data['status'][0]
        response = PetController.findPetByStatus(status)
        # Print the response details for debugging. To do so, please uncomment lines 28 and 29 in code.
        # jsonData = response.json()
        # print(json.dumps(jsonData, indent=4, sort_keys=True))
        self.assertEqual(response.status_code, 200, 'Expected status code 200 for findPetByStatus')

    def test_find_pet_by_status_single_pending_status(self):
        status = self.data['status'][1]
        response = PetController.findPetByStatus(status)
        # Print the response details for debugging. To do so, please uncomment lines 37 and 38 in code.
        # jsonData = response.json()
        # print(json.dumps(jsonData, indent=4, sort_keys=True))
        self.assertEqual(response.status_code, 200, 'Expected status code 200 for findPetByStatus')

    def test_find_pet_by_status_single_sold_status(self):
        status = self.data['status'][2]
        response = PetController.findPetByStatus(status)
        # Print the response details for debugging. To do so, please uncomment lines 46 and 47 in code.
        # jsonData = response.json()
        # print(json.dumps(jsonData, indent=4, sort_keys=True))
        self.assertEqual(response.status_code, 200, 'Expected status code 200 for findPetByStatus')

    # The following test is an example to get two statuses, but in reality it never happens.
    @unittest.skip("Skipping this test because it never happens in reality.")
    def test_find_pet_by_status_multiple_random_statuses(self):
        # Select 1 or 2 statuses randomly from the list
        status_list = sample(self.data['status'], 2)
        print(f"Selected statuses: {status_list}")
        response = PetController.findPetByStatus(status_list)
        # Print the response details for debugging
        jsonData = response.json()
        print(json.dumps(jsonData, indent=4, sort_keys=True))
        self.assertEqual(response.status_code, 200, 'Expected status code 200 for findPetByStatus')


if __name__ == '__main__':
    unittest.main()
