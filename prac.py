def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

    low_index = 0
    high_index = len(array) -1
    # use while loop to get middle index
    i = 0
    while low_index <= high_index:
        print(i)
        i += 1
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
binary_search_iterative(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 'N')
