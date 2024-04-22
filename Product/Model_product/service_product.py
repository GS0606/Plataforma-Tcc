from model_product import Product
from storage_product import ProductStorage

class ProductService:
    def __init__(self):
        self.storage = ProductStorage()

    def create_product(self, name, dest, quantity):
        new_product = Product(id=None, name=name, dest=dest, quantity=quantity)
        new_product_id = self.storage.create_product(new_product)
        return new_product_id
    
    def get_all_products(self):
        return self.storage.get_all_products()

    def get_product(self, product_id):
        return self.storage.get_product(product_id)

    def update_product(self, product_id, name, dest, quantity):
        update_client = Product(id=product_id,name=name, dest=dest, quantity=quantity)
        self.storage.update_product(update_client)

    def delete_product(self, product_id):
        self.storage.delete_product(product_id)

