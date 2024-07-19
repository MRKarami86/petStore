from src.services.store_service import StoreService
from src.models.store_model import StoreOrder

class StoreController:
    @staticmethod
    def returns_pet_inventories():
        return StoreService.returns_pet_inventories()

    @staticmethod
    def order_for_pet(order_data):
        # تبدیل دیکشنری به نمونه `StoreOrder`
        order = StoreOrder(**order_data)
        return StoreService.place_order(order.to_dict())