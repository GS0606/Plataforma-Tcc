import datetime

class Product:
    def __init__(self, name, id, dest, quantity, created_at=None, updated_at=None):
        self.name = name
        self.id = id 
        self.dest = dest
        self.quantity = quantity 
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()