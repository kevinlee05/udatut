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

def find_second(target, search):
    findfirst = search.find(target)
    startfindsecond = findfirst + len(target)
    findsecond = search.find(target, startfindsecond)
    return findsecond


# Test the function

import unittest

danton = "De l'audace, encore de l'audace, toujours de l'audace"
twister = "she sells seashells by the seashore"

class FindStringTest(unittest.TestCase):
    def test(self):
        self.assertEqual(find_second('zip', text), 18)
        self.assertEqual(find_second('zip', text2), -1)
        self.assertEqual(find_second('audace', danton), 25)
        self.assertEqual(find_second('she', twister), 13)

if __name__ == '__main__':
    unittest.main()

# IMPORTANT BEFORE SUBMITTING:
# You should only have one print command in your function












