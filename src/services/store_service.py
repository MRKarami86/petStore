import requests
from src.models.store_model import StoreOrder

class StoreService:
    BASE_URL = "https://petstore.swagger.io/v2"
    HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    @staticmethod
    def returns_pet_inventories():
        response = requests.get(f'{StoreService.BASE_URL}/store/inventory', headers=StoreService.HEADERS)
        return response

    @staticmethod
    def place_order(order_data):
        order = StoreOrder(
            id=order_data['id'],
            pet_id=order_data['petId'],
            quantity=order_data['quantity'],
            ship_date=order_data['shipDate'],
            status=order_data['status'],
            complete=order_data['complete']
        )
        response = requests.post(f"{StoreService.BASE_URL}/store/order", json=order.to_dict(), headers=StoreService.HEADERS)
        return response

    @staticmethod
    def find_purchase_order_by_ID(orderId):
        response = requests.get(f"{StoreService.BASE_URL}/store/order/{orderId}", headers=StoreService.HEADERS)
        return response

    @staticmethod
    def delete_purchase_order_by_ID(orderId):
        response = requests.delete(f"{StoreService.BASE_URL}/store/order/{orderId}", headers=StoreService.HEADERS)
        return response