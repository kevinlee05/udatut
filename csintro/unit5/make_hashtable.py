# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    i=0
    table = []
    while i < nbuckets:
        table.append([])
        i = i + 1
    return table


def make_hashtable2(nbuckets):
    # doesnt work because each element refers to the same list
    return [ [] ] * nbuckets

def make_hashtable3(nbuckets):
    table = []
    for e in range(0, nbuckets):
        table.append([])
    return table

assert make_hashtable(5) == make_hashtable2(5) # does not throw error

a = make_hashtable(5)
b = make_hashtable2(5)

assert a == b # no error


a[1].append([1])
b[1].append([1])

assert a == b # AssertionError

print(a)
print(b)
