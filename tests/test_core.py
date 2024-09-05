from time import sleep
import unittest
from core import RedisCore

class TestRedisCore(unittest.TestCase):

    def setUp(self):
        self.db = RedisCore()

    def test_set_and_get(self):
        self.db.set("name", "John")
        self.assertEqual(self.db.get("name"), "John")

    def test_expire(self):
        self.db.set("key", "value")
        self.db.expire("key", 1)
        self.assertEqual(self.db.get("key"), "value")
        sleep(2)
        self.assertIsNone(self.db.get("key"))

    def test_delete(self):
        self.db.set("age", 25)
        self.assertEqual(self.db.del_key("age"), 1)
        self.assertIsNone(self.db.get("age"))

if __name__ == "__main__":
    unittest.main()
