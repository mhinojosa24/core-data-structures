import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    text = text.isalnum() # removes all special characters and lowercase each letters
    start_index = 0
    end_index = len(text) - 1

    while start_index <= end_index:
        if text[start_index] != text[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    text = re.sub('[^A-Za-z0-9]+', '', text.lower())
    if text == '':
        return True

    if left is None and right is None:
        left, right = 0, len(text) - 1

    if text[left] != text[right]:
        return False

    else:
        left += 1
        right -= 1
        if left > right:
            return True
        return is_palindrome_recursive(text, left, right)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
