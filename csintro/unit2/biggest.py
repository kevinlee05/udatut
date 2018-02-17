# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.


def biggest(a, b, c):
    answer = a
    if b > a:
        answer = b
    if c > answer:
        answer = c
    return answer



# Test the function

import unittest

class FindStringTest(unittest.TestCase):
    def test(self):
        self.assertEqual(biggest(3,6,9),9)
        self.assertEqual(biggest(6,9,3),9)
        self.assertEqual(biggest(9,3,6),9)
        self.assertEqual(biggest(3,3,9),9)
        self.assertEqual(biggest(9,3,9),9)


if __name__ == '__main__':
    unittest.main()

#print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9
