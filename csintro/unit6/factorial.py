# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
    result = 1
    for i in range(n):
        result *= (i + 1)
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


assert factorial(0) == factorial_recursive(0)
#>>> 1

assert factorial(5) == factorial_recursive(5)
assert factorial(5) == 120
#>>> 120

assert factorial(10) == 3628800
assert factorial(10) == factorial_recursive(10)

for i in range(20):
    print(factorial(i))
    assert factorial(i) == factorial_recursive(i)
