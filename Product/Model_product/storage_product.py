import sqlite3
from model_product import Product
import datetime as datetime

class ProductStorage:
    def __init__(self, db_name='products.db'):
        self.db_name = db_name
        self.create_product_table()
        
    def connect_to_db(self):
        return sqlite3.connect(self.db_name)
    
    def create_product_table(self):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255) NOT NULL,
                    dest VARCHAR(255) NOT NULL,
                    quantity INTERGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            connection.commit()
    
    def create_product(self, product):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO product (name, dest, quantity)
                VALUES (?, ?, ?)
            """ , (product.name, product.dest, product.quantity))
            connection.commit()
            return cursor.lastrowid
            
    def get_all_products(self):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM product")
            rows = cursor.fetchall()
            products = [Product(*row) for row in rows]
            return products
        
    def get_product(self, product_id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM product WHERE id=?", (product_id,))
            row = cursor.fetchone()
            if row:
                return Product(*row)
            return None

    def update_product(self, product):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE product
                SET name=?, dest=?, quantity=?, updated_at=CURRENT_TIMESTAMP
                WHERE id=?
            """, (product.name, product.dest, product.quantity, product.id))
            connection.commit()

    def delete_product(self, product_id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM product WHERE id=?", (product_id,))
            connection.commit()
