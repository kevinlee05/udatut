# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    result = 1
    i = 0
    while i != n:
        i += 1
        result = result * i
    return result

def factorial2(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


# print factorial(4)
# #>>> 24
# print factorial(5)
# #>>> 120
# print factorial(6)
# #>>> 720

# Test the function

import unittest

class test(unittest.TestCase):
    def test(self):
        self.assertEqual(factorial(4),24)
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(6),720)

    def test2(self):
        self.assertEqual(factorial2(4),24)
        self.assertEqual(factorial2(5),120)
        self.assertEqual(factorial2(6),720)

if __name__ == '__main__':
    unittest.main()
