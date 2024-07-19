import unittest
import json
import os
from src.controllers.store_controller import StoreController

class TestDeletePurchaseOrderByID(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_delete_purchase_order_by_ID(self):
        orderId = self.data['order_pets']['id']
        response = StoreController.delete_purchase_order_by_ID(orderId)
        jsonData = response.json()
        # Print the response details for debugging. To do so, please uncomment lines 17 in code.
        print(json.dumps(jsonData, indent=4, sort_keys=True))
        self.assertEqual(response.status_code, 200, "Expected status code 200 for test find_purchase_order_by_ID")


if __name__ == '__main__':
    unittest.main()