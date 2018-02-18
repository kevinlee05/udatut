# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list, value):
    i = 0
    for item in list:
        if item == value:
            return i
        i +=1
    return -1

def find_element2(list, value):
    i = 0
    while i < len(list):
        if list[i] == value:
            return i
        i = i + 1
    return -1

def find_element3(list, value):
    if value in list:
        return list.index(value)
    return -1

def find_element4(list, value):
    if value not in list:
        return -1
    return list.index(value)

assert find_element([1,2,3],3) == 2
assert find_element(['alpha','beta'],'gamma') == -1
assert find_element2([1,2,3],3) == 2
assert find_element2(['alpha','beta'],'gamma') == -1
assert find_element3([1,2,3],3) == 2
assert find_element3(['alpha','beta'],'gamma') == -1
assert find_element4([1,2,3],3) == 2
assert find_element4(['alpha','beta'],'gamma') == -1

