import pytest
import timeit
import json
import os
from src.controllers.pet_controller import PetController


# خواندن داده‌ها از فایل JSON
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'dataTest.json'))
with open(file_path) as data_file:
    data = json.load(data_file)

pet_data = data['pet_add_body']

# تابع برای اضافه کردن پت
def add_pet():
    response = PetController.create_pet(pet_data['id'], pet_data['name'], pet_data['status'])
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    jsonData = response.json()
    assert jsonData["id"] == pet_data["id"], f"Returned pet ID does not match. Expected {pet_data['id']}, got {jsonData['id']}"
    assert jsonData["name"] == pet_data["name"], f"Returned pet name does not match. Expected {pet_data['name']}, got {jsonData['name']}"
    assert jsonData["status"] == pet_data["status"], f"Returned pet status does not match. Expected {pet_data['status']}, got {jsonData['status']}"

# تست پرفورمنس با استفاده از pytest
@pytest.mark.performance
def test_add_pet_performance():
    execution_time = timeit.timeit(add_pet, number=100)
    print(f"Average execution time over 100 iterations: {execution_time / 100} seconds")


if __name__ == "__main__":
    pytest.main(["-v", "test_add_pet_performance.py"])
