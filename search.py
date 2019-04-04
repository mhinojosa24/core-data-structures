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
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    # TODO: base case
    if array[index] == item:
        return index
    elif item not in array:
        return None

    # TODO: recursive case
    return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

    low_index = 0
    high_index = len(array) -1
    # use while loop to get middle index
    while low_index <= high_index:
        middle_index = (low_index + high_index) // 2
        if array[middle_index] == item:
            return middle_index # return index where item is found

        # check if the middle index item is greater than the item to look for
        # shift the high index of array
        if array[middle_index] > item:
            high_index = middle_index - 1

        # check if the middle index item is less than the item to look for
        # shift the low index of array
        if array[middle_index] < item:
            low_index = middle_index + 1

    return None # Not found

def binary_search_recursive(array, item, left=0, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

    if right is None:
        right = len(array) - 1

    if left > right:
        return None

    middle_index = (left + right) // 2
    if array[middle_index] == item:
        return middle_index # return index where item is found

    elif array[middle_index] > item:
        return binary_search_recursive(array, item, left, middle_index -1)

    elif array[middle_index] < item:
        return binary_search_recursive(array, item, middle_index + 1, right)
