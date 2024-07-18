import json
import unittest
from colorama import Fore, Style  # اضافه کردن کتابخانه colorama
import os
from src.controllers.pet_controller import PetController

class TestPetStoreContract(unittest.TestCase):

    def setUp(self):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'dataTest.json'))
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)

    def test_update_pet(self):
        pet_id = self.data['pet_id']
        UpdatePet = self.data['UpdatePet']

        response = PetController.modify_pet(pet_id, UpdatePet['name'], UpdatePet['status'])

        # Print JSON response with indentation and color
        if response.status_code == 200:
            print(f"{Fore.GREEN}JSON response:", json.dumps(response.json(), indent=4), "\n")
            print(f"{Fore.LIGHTBLUE_EX}Header response:", json.dumps(dict(response.headers), indent=4), "\n")
            print(Style.RESET_ALL)  # Reset colorama styles
        else:
            print(f"{Fore.RED}Error: Status Code {response.status_code}")
            print(Style.RESET_ALL)  # Reset colorama styles

        try:
            self.assertEqual(response.status_code, 200, "Expected status code 200 for update")
            self.assertEqual(response.json()["message"], f"{pet_id}", "Expected updated pet name")
        except AssertionError as e:
            print(f"{Fore.RED}AssertionError: {e}")
            print(Style.RESET_ALL)  # Reset colorama styles


if __name__ == "__main__":
    unittest.main()
