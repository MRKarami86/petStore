from src.models.pet_model import Pet
from src.services.pet_service import PetService

class PetController:
    @staticmethod
    def create_pet(pet_id, name, status):
        pet = Pet(pet_id, name, status)
        return PetService.add_pet(pet)

    @staticmethod
    def modify_pet(pet_id, name, status):
        pet = Pet(pet_id, name, status)
        return PetService.update_pet(pet_id, pet)

    @staticmethod
    def remove_pet(pet_id):
        return PetService.delete_pet(pet_id)

    @staticmethod
    def upload_image(pet_id, metadata, image_path):
        return PetService.upload_image(pet_id, metadata, image_path)
