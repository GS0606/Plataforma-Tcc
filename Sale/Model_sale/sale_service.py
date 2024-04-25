from sale_model import Sale, SaleItem, SaleStatus
from sale_storage import SaleStorage

class SaleService:
    def __init__(self):
        self.storage = SaleStorage()

    def create_sale(self, client_id, items):
        sale_id = self.storage.create_sale(client_id, items)
        return sale_id

    def update_sale_item_quantity(self, item_id, quantity):
        self.storage.update_sale_item_quantity(item_id, quantity)

    def finalize_sale(self, sale_id):
        self.storage.finalize_sale(sale_id)

    def get_sales_by_product(self, product_id):
        sales = self.storage.get_sales_by_product(product_id)
        return sales

    def get_sales_by_state(self, state_id):
        sales = self.storage.get_sales_by_state(state_id)
        return sales

    def cancel_sale(self, sale_id):
        self.storage.cancel_sale(sale_id)
