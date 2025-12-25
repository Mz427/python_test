import unittest
import algorithm_of_sorting

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.l_example = [5, 3, 8, 6, 7, 2]
        self.c_example = algorithm_of_sorting.AlgorithmOfSorting(self.l_example)


    def test_AlgorithmOfSorting(self):
        self.c_example.bubble_sort()
        self.assertEqual(self.c_example.l_to_sort, [2, 3, 5, 6, 7, 8])


if __name__ == "__main__":
    unittest.main()