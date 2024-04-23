import datetime

class SaleItem:
    def __init__(self, item_id, product_id, quantity, created_at, updated_at):
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()
    
        
    