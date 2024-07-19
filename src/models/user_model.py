
class User:
    def __init__(self, id, username, firstname, lastname, email, password, phone, userStatus):
        self.id = id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus

    def to_dict(self):
        return {
              "id": self.id,
              "username": self.username,
              "firstName": self.firstname,
              "lastName": self.lastname,
              "email": self.email,
              "password": self.password,
              "phone": self.phone,
              "userStatus": self.userStatus
            }