# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s == '':
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False


assert is_palindrome('') == True
assert is_palindrome('abab') == False
assert is_palindrome('andrea') == False
assert is_palindrome('abba') == True
assert is_palindrome('abaaba') == True
