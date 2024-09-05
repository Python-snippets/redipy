import time

class RedisCore:
    def __init__(self):
        self.store = {}
        self.expirations = {}
        
    def set(self, key, value):
        """set the value for the given key"""
        self.store[key] = value
        if key in self.expirations:
            del self.expirations[key]
        return "Ok"
    
    def get(self, key):
        """Get the value of a key, or return None if expired or doesn't exist"""
        if self.is_expired(key):
            self.del_key(key)
            return None
        return self.store.get(key, None)
    
    def del_key(self, key):
        """Delete a key from the store"""
        if key in self.store:
            del self.store[key]
        if key in self.expirations:
            del self.expirations[key]
        return 1 if key in self.store else 0

    def expire(self, key, ttl):
        """Set expiration time in seconds for a key"""
        if key in self.store:
            self.expirations[key] = time.time() + ttl
            return 1
        return 0

    def is_expired(self, key):
        """Check if a key has expired"""
        if key in self.expirations:
            if time.time() > self.expirations[key]:
                return True
        return False

    def keys(self):
        """List all keys in the store"""
        return list(self.store.keys())

    def persist(self, key):
        """Remove the expiration for a given key"""
        if key in self.expirations:
            del self.expirations[key]
            return 1
        return 0