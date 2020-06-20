"""
Given an integer, return True if it a Prime number otherwise return False.

Example 1
Input
n = 2

Output
True

"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def is_prime(n):
    if n>1:
        flag = 0
        for i in range(2,n):
            if n % i == 0:
                flag = 1
                break


        if flag == 0:
            return True

        else:
            return False

    return False
    pass                  


# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(is_prime(3), True)

    def test_02(self):
        self.assertEqual(is_prime(12), False)

    def test_03(self):
        self.assertEqual(is_prime(33), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
