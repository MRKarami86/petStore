import requests

class StoreService:
    BASE_URL = "https://petstore.swagger.io/v2"
    HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    @staticmethod
    def returns_pet_inventories():
        response = requests.get(f'{StoreService.BASE_URL}/store/inventory', headers=StoreService.HEADERS)
        return response

    @staticmethod
    def place_order(order):
        response = requests.post(f"{StoreService.BASE_URL}/store/order", json=order, headers=StoreService.HEADERS)
        return response