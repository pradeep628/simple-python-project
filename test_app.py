
import unittest
from app import multiply  # make sure app.py has a function named multiply

class TestApp(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

if __name__ == "__main__":
    unittest.main()
