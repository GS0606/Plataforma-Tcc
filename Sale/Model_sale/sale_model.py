import datetime

class Sale:
    def __init__(self, sale_id, client_id, items, status, created_at, updated_at):
        self.sale_id = sale_id
        self.client_id = client_id
        self.items = items
        self.status = status
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()

