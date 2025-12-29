import unittest
import random
import algorithm_of_sorting

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.l_example = [random.randint(1, 10) for _ in range(10)]

    def test_AlgorithmOfSorting(self):
        self.assertEqual(sorted(self.l_example), algorithm_of_sorting.bubble_sort(self.l_example[:]))

if __name__ == "__main__":
    unittest.main()