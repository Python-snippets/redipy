from core import RedisCore

class RedisCommands:
    def __init__(self):
        self.db = RedisCore()

    def handle_command(self, command, *args):
        """Handle a command from the user"""
        if command == "SET":
            ttl = int(args[2]) if len(args) > 2 else None  # Optional TTL argument
            return self.db.set(args[0], args[1], ttl)
        elif command == "GET":
            return self.db.get(args[0])
        elif command == "DEL":
            return self.db.del_key(args[0])
        elif command == "EXPIRE":
            return self.db.expire(args[0], int(args[1]))
        elif command == "KEYS":
            return self.db.keys()
        elif command == "PERSIST":
            return self.db.persist(args[0])
        else:
            return "Unknown command"
