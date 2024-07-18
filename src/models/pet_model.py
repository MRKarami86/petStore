class Pet:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def to_dict(pet):
        return {
            "id": pet.id,
            "name": pet.name,
            "status": pet.status
        }