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

    # recursive case
    return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):

    low_bound = 0
    high_bound = len(array) -1
    # use while loop to go through the whole array
    while low_bound <= high_bound:
        middle_bound = (low_bound + high_bound) // 2
        if array[middle_bound] == item:
            return middle_bound # return index where item is found

        # check if the middle index item is greater than the item to look for
        if array[middle_bound] > item:
            high_bound = middle_bound - 1 # shift the high index of array

        # check if the middle index item is less than the item to look for
        if array[middle_bound] < item:
            low_bound = middle_bound + 1 # shift the low index of array

    return None # Not found

def binary_search_recursive(array, item, left=None, right=None):

    if left is None and right is None:
        left, right = 0, len(array) - 1

    if left > right:
        return None

    middle_bound = (left + right) // 2
    if array[middle_bound] == item:
        return middle_bound # return index where item is found

    elif array[middle_bound] > item:
        right = middle_bound - 1
        return binary_search_recursive(array, item, left, right)

    elif array[middle_bound] < item:
        left = middle_bound + 1
        return binary_search_recursive(array, item, left, right)
