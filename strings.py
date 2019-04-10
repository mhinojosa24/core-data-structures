def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

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

    txt_index = 0 # keeps track of each character position in text
    pat_index = 0 # keeps track of each character position in pattern

    # edge case for empty string
    if pattern == '' or text == pattern:
        return 0

    # once the text index is the same as the length of text, this will stop
    while txt_index != len(text):
        if text[txt_index] == pattern[pat_index]: # checks if both characters are the same
            if pat_index == len(pattern) - 1: # found valid pattern
                return txt_index - pat_index # returns the starting position of the pattern
            pat_index += 1
        else:
            txt_index -= pat_index
            pat_index = 0
        txt_index += 1


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    txt_index = 0 # keeps track of each character position in text
    pat_index = 0 # keeps track of each character position in pattern
    result = []

    # edge case for empty string pattern
    if pattern == '':
        for index in range(len(text)):
            result.append(index)
        return result

    # edge case for singular pattern
    for index, letter in enumerate(text):
        if text[index] == pattern:
            result.append(index)
    return result

    # once the text index is the same as the length of text, this will stop
    while txt_index != len(text):
        if text[txt_index] == pattern[pat_index]:
            if pat_index == len(pattern) - 1: # once the current pattern index equals the length of pattern, you have officially found a valid pattern
                result.append(txt_index - pat_index) # save / append the start of pattern
            pat_index += 1
        else:
            txt_index -= pat_index # restart index to 0
            pat_index = 0 # restart index to 0
        txt_index += 1 # shift index to next
    return result

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    # indexes = find_all_indexes(text, pattern)
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
