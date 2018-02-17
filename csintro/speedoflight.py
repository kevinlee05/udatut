# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"
text2 = 'all zip files are compressed'

# ENTER CODE BELOW HERE

def findsecondstringin(string, text):
    findfirst = text.find(string)
    startfindsecond = findfirst + len(string)
    findsecond = text.find(string, startfindsecond)
    print(findsecond)
    return findsecond


# Test the function

import unittest

class FindStringTest(unittest.TestCase):
    def test(self):
        print(text)
        self.assertEqual(findsecondstringin('zip', text), 18)
        self.assertEqual(findsecondstringin('zip', text2), -1)

if __name__ == '__main__':
    unittest.main()

# IMPORTANT BEFORE SUBMITTING:
# You should only have one print command in your function












