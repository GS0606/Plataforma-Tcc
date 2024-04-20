from model_client import Client
from storage_client import ClientStorage

class ClientService:
    def __init__(self):
        self.storage = ClientStorage()

    def create_client(self, name, surname, email, data_nascimento):
        new_client = Client(id=None, name=name, surname=surname, email=email, data_nascimento=data_nascimento)
        new_client_id = self.storage.create_client(new_client)
        return new_client_id

    def get_client(self, client_id):
        return self.storage.get_client(client_id)

    def update_client(self, client_id, name, surname, email, data_nascimento):
        updated_client = Client(id=client_id, name=name, surname=surname, email=email, data_nascimento=data_nascimento)
        self.storage.update_client(updated_client)

    def delete_client(self, client_id):
        self.storage.delete_client(client_id)

