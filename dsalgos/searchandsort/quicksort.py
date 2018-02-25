"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    left = 0
    right = len(array) -1
    pivot = int((left + right) /2)
    print(array, left, pivot, right)
    sortpartition(array, left, right, pivot)
    return array

def sortpartition(array, left, right, pivot):
    if right - left == 1:
        if array[left] > array[right]:
            array[left], array[right] = array[right], array[left]
        return
    if pivot == left or pivot == right:
        return
    tempright = right
    for i in range(left, int(pivot + 1)):
        if array[i] > array[tempright]:
            array[i], array[tempright] = array[tempright], array[i]
        if array[i] > array[pivot]:
            array[i], array[pivot] = array[pivot], array[i]
        if array[tempright] < array[pivot]:
            array[tempright], array[pivot] = array[pivot], array[tempright]
        tempright -= 1
        i += 1
    print(array, left , pivot, right)
    sortpartition(array, left, pivot, int((left+pivot)/2 ))
    sortpartition(array, pivot, right, int((right+pivot)/2) )

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
test2 = [21, 4, 1, 405, 54, 9, 20, 25, 6, 2, 14,8, 104, 29]
print(quicksort(test2))

