from helper import find_pattern

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # time complexity: O(n) => goes through each character in string

    txt_index = 0 # keeps track of each character position in text
    pat_index = 0 # keeps track of each character position in pattern

    # edge case for empty string or if the pattern matches the text
    if pattern == '' or text == pattern:
        return True

    # once the text index is the same as the length of text, this will stop
    while txt_index != len(text):
        if text[txt_index] == pattern[pat_index]:
            if pat_index == len(pattern) - 1:
                return True
            pat_index += 1
        else:
            txt_index -= pat_index
            pat_index = 0
        txt_index += 1
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Time complexity: O(n) => goes through each character in string
    # Space complexity: O(1) => appends to array for each found pattern
    result = find_pattern(text, pattern)# returns the beginning of each pattern in array

    if result == []:
        return None
    else:
        return result[0] # return the first found pattern


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Time complexity: O(n) => goes through each character in string
    # Space complexity: O(1) => appends to array for each found pattern

    return find_pattern(text, pattern) # returns the beginning of each pattern in array

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
