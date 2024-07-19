# src/models/store_model.py

class StoreOrder:
    def __init__(self, id, pet_id, quantity, ship_date, status, complete):
        self.id = id
        self.pet_id = pet_id
        self.quantity = quantity
        self.ship_date = ship_date
        self.status = status
        self.complete = complete

    def to_dict(self):
        return {
            "id": self.id,
            "petId": self.pet_id,
            "quantity": self.quantity,
            "shipDate": self.ship_date,
            "status": self.status,
            "complete": self.complete
        }
