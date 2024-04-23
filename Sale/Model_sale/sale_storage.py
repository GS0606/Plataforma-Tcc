import sqlite3
from sale_model import Sale
from status_model import SaleStatus
from Sale.Model_sale.SaleItem import SaleItem
from datetime import datetime  

class SaleStorage:
    def __init__(self, db_name='sales.db'):
        self.db_name = db_name
        self.create_sale_table()
        
    def connect_to_db(self):
        return sqlite3.connect(self.db_name)
    
    def create_sale_table(self):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sale (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    status INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (client_id) REFERENCES client(id)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sale_item (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sale_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    FOREIGN KEY (sale_id) REFERENCES sale(id),
                    FOREIGN KEY (product_id) REFERENCES product(id)
                )
            """)
            connection.commit()
    
    def create_sale(self, client_id, items):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO sale (client_id, status)
                VALUES (?, ?)
            """ , (client_id, SaleStatus.STARTED))
            sale_id = cursor.lastrowid
            self.add_items_to_sale(connection, sale_id, items)
            return sale_id
    
    def add_items_to_sale(self, connection, sale_id, items):
        cursor = connection.cursor()
        for item in items:
            cursor.execute("""
                INSERT INTO sale_item (sale_id, product_id, quantity)
                VALUES (?, ?, ?)
            """ , (sale_id, item.product_id, item.quantity))
        connection.commit()

    def update_sale_item_quantity(self, sale_id, item_id, quantity):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE sale_item
                SET quantity=?
                WHERE id=?
            """, (quantity, item_id))
            connection.commit()

    def finalize_sale(self, sale_id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE sale
                SET status=?, updated_at=CURRENT_TIMESTAMP
                WHERE id=?
            """, (SaleStatus.DONE, sale_id))
            connection.commit()

    def get_sales_by_product(self, product_id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT sale.id, sale.client_id, sale.status, sale.created_at, sale.updated_at
                FROM sale
                JOIN sale_item ON sale.id = sale_item.sale_id
                WHERE sale_item.product_id=?
            """, (product_id,))
            rows = cursor.fetchall()
            sales = [Sale(*row) for row in rows]
            return sales

    def get_sales_by_state(self, state_id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM sale WHERE status=?
            """, (state_id,))
            rows = cursor.fetchall()
            sales = [Sale(*row) for row in rows]
            return sales

    def cancel_sale(self, sale_id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE sale
                SET status=?, updated_at=CURRENT_TIMESTAMP
                WHERE id=?
            """, (SaleStatus.CANCELED, sale_id))
            connection.commit()
