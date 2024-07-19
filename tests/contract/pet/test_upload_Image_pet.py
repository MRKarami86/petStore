import unittest
import json
import os
from src.controllers.pet_controller import PetController

class test_uploadImage_pet(unittest.TestCase):

    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_uploadImage(self):
        upload_image_data = self.data['upload_image_data']
        response = PetController.upload_image(upload_image_data['pet_id'], upload_image_data['metadata'], upload_image_data['image_path'])
        self.assertEqual(response.status_code, 200, "Expected status code 200 for upload image")

        jsonData = response.json()
        self.assertEqual(jsonData['code'], 200)
        print("\n" + json.dumps(jsonData, indent=4, sort_keys=True))


if __name__ == '__main__':
    unittest.main()