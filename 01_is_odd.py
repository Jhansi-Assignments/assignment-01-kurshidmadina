"""
Given an integer, return True if it odd otherwise return False.

Example 1
Input
n = 2

Output
False

"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def is_odd(n):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestIsOdd(unittest.TestCase):

    def test_01(self):
        self.assertEqual(is_odd(3), True)

    def test_02(self):
        self.assertEqual(is_odd(12), False)

    def test_03(self):
        self.assertEqual(is_odd(33), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
