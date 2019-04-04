"""
This file is for testing the Fibonacci class
"""

import unittest
from fibonacci import Fibonacci

class FibonacciTestCase(unittest.TestCase):

    def setUp(self):
        self.test_cases = {0:"n has to be integer and greather than 0", 1:1, 2:1, 10:55, 25:75025, 35:9227465, 40:102334155}

    def test_recursive_algorithm(self):
        """
        The objective of this test is checking the fibonacci_recursive()
        method returns correct values.
        """
        for test in self.test_cases:
            print(test)
            my_fibonacci = Fibonacci(test)
            self.assertEqual(self.test_cases[test], my_fibonacci.fibonacci_recursive(), f"Should be {self.test_cases[test]}")

    def test_not_recursive_algorithm(self):
        for test in self.test_cases:
            my_fibonacci = Fibonacci(test)
            self.assertEqual(self.test_cases[test], my_fibonacci.fibonacci_not_recursive(), f"Should be {self.test_cases[test]}")


if __name__ == '__main__':
    unittest.main()