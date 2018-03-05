"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    firstindex = 0
    lastindex = len(input_array) -1
    midindex = int((firstindex + lastindex) / 2)
    while True:
        #print firstindex, midindex, lastindex, input_array[midindex], value
        if (midindex == lastindex) or (midindex == firstindex):
            return -1
        if input_array[midindex] == value:
            return midindex
        if input_array[midindex] > value:
            lastindex = midindex
        else:
            firstindex = midindex
        midindex = int((firstindex + lastindex) / 2)

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
