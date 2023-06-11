from cgi import test
import unittest
from src.models import ducks

class DuckTest(unittest.TestCase):
    def test_object_creation(self):
        testDuck = ducks.Duck("test", 100, "green", "Male")
        self.assertIsNotNone(testDuck)

if __name__ == '__name__':
    unittest.main()