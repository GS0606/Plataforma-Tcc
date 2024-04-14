import sqlite3
from Model_client.model_client import Client
import datetime as datetime

import sqlite3
import datetime

class ClientStorage:
    def __init__(self, db_name='clients.db'):
        self.db_name = db_name

    def connect_to_db(self):
        return sqlite3.connect(self.db_name)

    def create_client_table(self):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS client (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255) NOT NULL,
                    surname VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    data_nascimento TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            connection.commit()

    def create_client(self, client):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO client (name, surname, email, data_nascimento)
                VALUES (?, ?, ?, ?)
            """, (client.name, client.surname, client.email, client.data_nascimento))
            connection.commit()
            return cursor.lastrowid

    def get_client(self, client_id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM client WHERE id=?", (client_id,))
            row = cursor.fetchone()
            if row:
                return Client(*row)
            return None

    def update_client(self, client):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE client
                SET name=?, surname=?, email=?, data_nascimento=?, updated_at=CURRENT_TIMESTAMP
                WHERE id=?
            """, (client.name, client.surname, client.email, client.data_nascimento, client.id))
            connection.commit()

    def delete_client(self, client_id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM client WHERE id=?", (client_id,))
            connection.commit()

# Exemplo de uso:
if __name__ == "__main__":
    # Criando a tabela client
    client_storage = ClientStorage()
    client_storage.create_client_table()

    # # Criando um novo cliente
    # new_client = Client(id=None, name="João", surname="Silva", email="joao@example.com", data_nascimento="1990-01-01")
    # new_client_id = client_storage.create_client(new_client)
    # print("Novo cliente criado com ID:", new_client_id)

    # # Obtendo o cliente recém-criado
    # retrieved_client = client_storage.get_client(new_client_id)
    # print("Cliente obtido do banco de dados:", retrieved_client.__dict__)

    # # Atualizando o cliente
    # retrieved_client.name = "João Novo"
    # client_storage.update_client(retrieved_client)

    # # Deletando o cliente
    # client_storage.delete_client(new_client_id)
    # print("Cliente deletado.")
