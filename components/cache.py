# Caches frequently accessed data to reduce database load.

class Cache:
    def __init__(self, size: int):
        self.size = size
        self.store = {}
        self.access_order = []

