import os.path
import unittest
from src.controllers.store_controller import StoreController
import json

class TestReturnsPetInventoriesByStatus(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_returns_pet_inventories(self):
        dataReturns = self.data['returns_pet_inventories']
        response = StoreController.returns_pet_inventories()
        jsonData = response.json()
        # Print the response details for debugging. To do so, please uncomment lines 17 in code.
        # print(json.dumps(jsonData, indent=4, sort_keys=True))
        self.assertEqual(response.status_code, 200, 'Expected status code 200 for Returns Pet Inventories By Status')
        self.assertIn(dataReturns[1], jsonData, 'Expected Pending JSON Data for Returns Pet Inventories')
        self.assertIn(dataReturns[2], jsonData, 'Expected available JSON Data for Returns Pet Inventories')
        self.assertIn(dataReturns[6], jsonData, 'Expected sold JSON Data for Returns Pet Inventories')

        for item in dataReturns:
            self.assertIn(item, jsonData, f'Expected {item} in JSON Data for Returns Pet Inventories')


if __name__ == '__main__':
    unittest.main()