import datetime

class Sale:
    def __init__(self, sale_id, client_id, items, status, created_at, updated_at):
        self.sale_id = sale_id
        self.client_id = client_id
        self.items = items
        self.status = status
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()

class SaleItem:
    def __init__(self, item_id, product_id, quantity):
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity

class SaleStatus:
    STARTED = 0
    PROGRESS = 1
    DONE = 2
    CANCELED = 3