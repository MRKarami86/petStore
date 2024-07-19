import unittest
import json
import os
from src.controllers.pet_controller import PetController

class TestFindPetById(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_find_pet_by_id(self):
        pet_id = self.data['pet_id']
        response = PetController().FindPetById(pet_id)
        self.assertEqual(response.status_code, 200, 'Expected status code 200 for FindPetById')

        jsonData = response.json()
        self.assertEqual(jsonData['id'], self.data['pet_id'], f'Expected pet_id to be equal to the {pet_id}')


if __name__ == '__main__':
    unittest.main()

