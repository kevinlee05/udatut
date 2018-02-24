# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    #recursive algorithm is very resource intensive and slow compared to iterative algorithm
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 2
    fibA = 0
    fibB = 1
    temp = 0
    while True:
        temp = fibA + fibB
        fibA = fibB
        fibB = temp
        if i == n - 1:
            return fibA + fibB
        i += 1

def fibonacci3(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

#calculate when mass of rabbits will exceed the mass of the earth
mass_of_earth = 5.972 * 10**24 # kilograms
mass_of_rabbit = 2 # 2 kilograms per rabbit

n = 1
while fibonacci3(n) * mass_of_rabbit < mass_of_earth:
    n = n + 1
print(n, fibonacci3(n))

#print fibonacci2(0)
#>>> 0
#print fibonacci2(1)
#>>> 1
#print fibonacci2(15)
#>>> 610
