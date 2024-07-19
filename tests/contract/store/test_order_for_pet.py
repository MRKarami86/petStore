import unittest
import json
import os
from src.controllers.store_controller import StoreController

class TestOrderForPets(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_order_for_pets(self):
        order_pet = self.data['order_pets']
        response = StoreController.order_for_pet(order_pet)
        jsonData = response.json()
        # df
        print(jsonData)


if __name__ == '__main__':
    unittest.main()