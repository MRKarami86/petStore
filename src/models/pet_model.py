class Pet:
    def __init__(self, id, category, name, photoUrls, tags, status):
        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "name": self.name,
            "photoUrls": self.photoUrls,
            "tags": self.tags,
            "status": self.status
        }
