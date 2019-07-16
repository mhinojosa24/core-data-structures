#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):

    # base case
    if array[index] == item:
        return index
    elif item not in array:
        return None
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == item:
            return middle

        if item < array[middle]:
            right = middle - 1
            
        if item > array[middle]:
            left = middle + 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if left > right:
        return None

    middle = (left + right) // 2
    if array[middle] == item:
        return middle

    elif item < array[middle]:
        right = middle - 1
        return binary_search_recursive(array, item, left, right)

    elif item > array[middle]:
        left = middle + 1
        return binary_search_recursive(array, item, left, right)
