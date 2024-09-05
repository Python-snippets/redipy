import time

class RedisCore:
    def __init__(self):
        self.store = {}
        self.expirations = {}
        
    def set(self, key, value):
        """set the value for the given key"""
        self.store[key] = value
        if key in self.exipirations:
            del self.expirataions[key]
        return "Ok"
    
    