import requests
from src.models.user_model import User

class UserService:
    BASE_URL = "https://petstore.swagger.io/v2"
    HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    @staticmethod
    def create_user(user):
        userِData = User(
            id=user['id'],
            username=user['username'],
            firstname=user['firstName'],
            lastname=user['lastName'],
            email=user['email'],
            password=user['password'],
            phone=user['phone'],
            userStatus=user['userStatus']
        )
        response = requests.post(f"{UserService.BASE_URL}/user", json=userِData.to_dic(), headers=UserService.HEADERS)
        return response

    @staticmethod
    def create_user_with_array(users):
        user_data_list = [
            User(
                id=user['id'],
                username=user['username'],
                firstname=user['firstName'],
                lastname=user['lastName'],
                email=user['email'],
                password=user['password'],
                phone=user['phone'],
                userStatus=user['userStatus']
            ).to_dict() for user in users
        ]
        response = requests.post(f"{UserService.BASE_URL}/user/createWithArray", json=user_data_list,headers=UserService.HEADERS)
        return response