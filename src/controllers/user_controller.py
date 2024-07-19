from src.services.user_service import UserService

class UserController:

    @staticmethod
    def create_user(user):
        return UserService.create_user(user)

    @staticmethod
    def create_user_with_array(users):
        return UserService.create_user_with_array(users)