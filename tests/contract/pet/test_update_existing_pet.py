import unittest
import os
import json
from src.controllers.pet_controller import PetController
from src.models.pet_model import Pet

class TestUpdateExistingPet(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_update_existing_pets(self):
        pet_data = self.data['updateExistingPet']
        pet = Pet(
            id=pet_data['id'],
            category=pet_data['category'],
            name=pet_data['name'],
            photoUrls=pet_data['photoUrls'],
            tags=pet_data['tags'],
            status=pet_data['status']
        )
        response = PetController.updateExistingPets(pet)
        jsonData = response.json()
        # Print the response details for debugging. To do so, please uncomment lines 26 in code.
        # print(json.dumps(jsonData, indent=4, sort_keys=True))
        self.assertEqual(response.status_code, 200, 'Status Code should be 200')

        self.assertEqual(jsonData['id'], pet.id, f'Status Code should be {pet.id}')
        self.assertEqual(jsonData['status'], pet.status, f'Status Code should be {pet.status}')
        self.assertEqual(jsonData['name'], pet.name, f'Status Code should be {pet.name}')


if __name__ == '__main__':
    unittest.main()
