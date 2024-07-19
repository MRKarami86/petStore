import unittest
import json
import os
from src.controllers.user_controller import UserController

class TestDeletePurchaseOrderByID(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_create_user(self):
        user = self.data['create_user']
        responce = UserController.create_user(user)
        jsonData = responce.json()
        print(json.dumps(jsonData, indent=4, sort_keys=True))
        self.assertEqual(responce.status_code, 200)


if __name__ == '__main__':
    unittest.main()