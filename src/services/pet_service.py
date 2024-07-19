import requests
from src.models.pet_model import Pet
from urllib.parse import urlencode

class PetService:
    BASE_URL = "https://petstore.swagger.io/v2"
    HEADERS = {'Content-Type': 'application/json'}

    @staticmethod
    def add_pet(pet):
        response = requests.post(f"{PetService.BASE_URL}/pet", json=Pet.to_dict(pet), headers=PetService.HEADERS)
        return response

    @staticmethod
    def update_pet(pet_id, pet):
        petData = urlencode(Pet.to_dict(pet))
        response = requests.post(f"{PetService.BASE_URL}/pet/{pet_id}", data=petData, headers={'Content-Type':'application/x-www-form-urlencoded'})
        return response

    @staticmethod
    def delete_pet(pet_id):
        response = requests.delete(f"{PetService.BASE_URL}/pet/{pet_id}", headers=PetService.HEADERS)
        return response

    @staticmethod
    def upload_image(pet_id, metadata, image_path):
        with open(image_path, 'rb') as image_file:
            response = requests.post(f"{PetService.BASE_URL}/pet/{pet_id}/uploadImage", files={'file': image_file},
                                     data={'additionalMetadata': metadata})
        return response

    @staticmethod
    def findPetById(pet_id):
        response = requests.get(f"{PetService.BASE_URL}/pet/{pet_id}", headers=PetService.HEADERS)
        return response

    @staticmethod
    def findPetByStatus(status):
        if isinstance(status, list):
            # If status is a list, convert it to a suitable query string
            status_param = '&'.join(f"status={s}" for s in status)
        else:
            # If status is a single string, just use it
            status_param = f"status={status}"

        response = requests.get(f"{PetService.BASE_URL}/pet/findByStatus?{status_param}", headers=PetService.HEADERS)
        return response

    @staticmethod
    def updateExistingPets(updatedPet):
        petData = updatedPet.to_dict()
        response = requests.put(f"{PetService.BASE_URL}/pet", json=petData, headers=PetService.HEADERS)
        return response