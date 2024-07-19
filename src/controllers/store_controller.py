from src.services.store_service import StoreService


class StoreController:
    @staticmethod
    def returns_pet_inventories():
        return StoreService.returns_pet_inventories()

    @staticmethod
    def order_for_pet(order_data):
        return StoreService.place_order(order_data)

    @staticmethod
    def find_purchase_order_by_ID(orderId):
        return StoreService.find_purchase_order_by_ID(orderId)

    @staticmethod
    def delete_purchase_order_by_ID(orderId):
        return StoreService.delete_purchase_order_by_ID(orderId)