import unittest
import json
import os
from src.controllers.pet_controller import PetController

class AddPetTest(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_add_pet(self):
        pet_data = self.data['pet_add_body']
        response = PetController.create_pet(pet_data['id'], pet_data['name'], pet_data['status'])
        self.assertEqual(response.status_code, 200, "Expected status code 200 for adding pet")

        jsonData = response.json()
        self.assertEqual(jsonData["id"], pet_data["id"], "Returned pet ID does not match")
        self.assertEqual(jsonData["name"], pet_data["name"], "Returned pet name does not match")
        self.assertEqual(jsonData["status"], pet_data["status"], "Returned pet status does not match")


if __name__ == '__main__':
    unittest.main()
