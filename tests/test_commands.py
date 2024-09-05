import unittest
from commands import RedisCommands

class TestRedisCommands(unittest.TestCase):

    def setUp(self):
        self.commands = RedisCommands()

    def test_set_and_get_command(self):
        self.commands.handle_command("SET", "name", "Alice")
        self.assertEqual(self.commands.handle_command("GET", "name"), "Alice")

    def test_delete_command(self):
        self.commands.handle_command("SET", "age", "30")
        self.assertEqual(self.commands.handle_command("DEL", "age"), 1)
        self.assertIsNone(self.commands.handle_command("GET", "age"))

if __name__ == "__main__":
    unittest.main()
