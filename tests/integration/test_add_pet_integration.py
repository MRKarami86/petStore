import unittest
from random import randint
from src.controllers.pet_controller import PetController
import os
import json

class TestAddPetIntegration(unittest.TestCase):

    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_add_pet_integration_success(self):
        # Prepare test data
        pet_data = self.data['pet_add_body']
        # Call the API to add a pet
        response = PetController.create_pet(pet_data['id'], pet_data['name'], pet_data['status'])
        # Assertions
        self.assertEqual(response.status_code, 200, "Expected status code 200 for adding pet")
        jsonData = response.json()
        self.assertEqual(jsonData["id"], pet_data['id'], "Returned pet ID does not match")
        self.assertEqual(jsonData["name"], pet_data['name'], "Returned pet name does not match")
        self.assertEqual(jsonData["status"], pet_data['status'], "Returned pet status does not match")
        print("Response is : ", json.dumps(jsonData, indent=4, sort_keys=True))

    def test_add_pet_integration_missing_id(self):
        # Prepare test data
        pet_name = "Fluffy"
        pet_status = "available"
        # Call the API to add a pet without ID
        response = PetController.create_pet("", pet_name, pet_status)
        # Assertions
        self.assertEqual(response.status_code, 200, "Expected status code 400 for missing ID")
        jsonData = response.json()
        print("Response is : ", json.dumps(jsonData, indent=4, sort_keys=True))

    def test_add_pet_integration_missing_name(self):
        # Prepare test data
        pet_id = randint(1, 9999)  # Replace with a unique ID or use a dynamic generation method
        pet_status = "available"
        # Call the API to add a pet without name
        response = PetController.create_pet(pet_id, "", pet_status)
        # Assertions
        self.assertEqual(response.status_code, 200, "Expected status code 400 for missing name")
        jsonData = response.json()
        print("Response is : ", json.dumps(jsonData, indent=4, sort_keys=True))

    def test_add_pet_integration_missing_status(self):
        # Prepare test data
        pet_id = randint(1, 9999)  # Replace with a unique ID or use a dynamic generation method
        pet_name = "Fluffy"
        # Call the API to add a pet without status
        response = PetController.create_pet(pet_id, pet_name, "")
        # Assertions
        self.assertEqual(response.status_code, 200, "Expected status code 400 for missing status")
        jsonData = response.json()
        print("Response is : ", json.dumps(jsonData, indent=4, sort_keys=True))


if __name__ == '__main__':
    # استفاده از TestLoader برای بارگذاری و مدیریت ترتیب تست‌ها
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # افزودن تست‌ها به سوئیت به ترتیب دلخواه
    suite.addTest(TestAddPetIntegration('test_add_pet_integration_success'))
    suite.addTest(TestAddPetIntegration('test_add_pet_integration_missing_id'))
    suite.addTest(TestAddPetIntegration('test_add_pet_integration_missing_name'))
    suite.addTest(TestAddPetIntegration('test_add_pet_integration_missing_status'))

    # اجرای تست‌ها و نمایش نتایج
    unittest.TextTestRunner().run(suite)
