import unittest
import json
import os
import requests
from src.controllers.pet_controller import PetController

class DeletePetTest(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_delete_pet(self):
        pet_id = self.data['pet_id']
        response = PetController.remove_pet(pet_id)
        self.assertIn(response.status_code, [200, 204], "Expected status code 200 or 204 for deleting pet")

        response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}", headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404, "Expected status code 404 for fetching deleted pet")

if __name__ == '__main__':
    unittest.main()
