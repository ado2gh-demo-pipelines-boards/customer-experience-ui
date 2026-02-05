import unittest
from api import app

class TestApp(unittest.TestCase):
    def test_health(self):
        self.assertEqual(app.health()["status"], "ok")

    def test_add(self):
        self.assertEqual(app.add(2,3), 5)

if __name__ == "__main__":
    unittest.main()


    def test_mul(self):
        self.assertEqual(app.mul(2,3), 6)

