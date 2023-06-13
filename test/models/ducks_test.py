from cgi import test
import unittest
from src.models import ducks

class DuckTest(unittest.TestCase):

    testName = "TestDuck"
    testWeight = 100
    testColor = "Yellow"
    testsex = "Male"

    def test_object_creation(self):
        testDuck = ducks.Duck("test", 100, "green", "Male")
        self.assertIsNotNone(testDuck)

    #Test your Successes 
    def test_eat_method_pass(self):
        testDuck1 = ducks.Duck(self.testName, self.testWeight, self.testColor, self.testsex)
        testDuck1.eat()

        expected = 101
        actual = testDuck1.weight

        self.assertEqual(expected, actual)

    #Test to make sure it fails like it supposed to
    def test_eat_method_fail(self):
        testDuck1 = ducks.Duck(self.testName, self.testWeight, self.testColor, self.testsex)
        testDuck1.eat()

        expected = 0
        actual = testDuck1.weight

        self.assertNotEqual(expected, actual)

    def test_die_method_alive(self):
        testDuck1 = ducks.Duck(self.testName, self.testWeight, self.testColor, self.testsex)

        self.assertTrue(testDuck1.isAlive)

    def test_die_method_dead(self):
        testDuck1 = ducks.Duck(self.testName, self.testWeight, self.testColor, self.testsex)
        testDuck1.die()

        self.assertFalse(testDuck1.isAlive)


    def test_revive_method_alive(self):
        testDuck1 = ducks.Duck(self.testName, self.testWeight, self.testColor, self.testsex)
        testDuck1.die()
        testDuck1.live()

        self.assertTrue(testDuck1.isAlive)

    def test_revive_method_alive2(self):
        testDuck1 = ducks.Duck(self.testName, self.testWeight, self.testColor, self.testsex)
        testDuck1.live()

        self.assertTrue(testDuck1.isAlive)

    

    
    


if __name__ == '__main__':
    unittest.main()