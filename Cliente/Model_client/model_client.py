import datetime

class Client:
    def __init__(self, id, name, surname, email, data_nascimento, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.data_nascimento = data_nascimento
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()