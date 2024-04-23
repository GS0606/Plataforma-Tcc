import sqlite3
from model_client import Client
import datetime as datetime

class ClientStorage:
    def __init__(self, db_name='clients.db'):
        self.db_name = db_name
        self.create_client_table()

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
        
    def get_all_clients(self):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM client")
            rows = cursor.fetchall()
            clients = [Client(*row) for row in rows]
            return clients

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


