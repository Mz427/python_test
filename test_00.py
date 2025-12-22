import unittest
import hello_world

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.hello = hello_world.HelloWorld(1, 5)
    def test_add(self):
        self.assertEqual(self.hello.add(), 6)
    def test_minus(self):
        self.assertEqual(self.hello.minus(), -4)
if __name__ == "__main__":
    unittest.main()