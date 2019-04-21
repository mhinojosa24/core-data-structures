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
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # Time: O(n)
    # Space: O(1)

    left = 0
    right = len(text) - 1

    while left <= right:
        if not text[left].isalpha() and text[left] != '': # checks if the character is not in the alphabet
            left += 1 # skips character
            continue

        if not text[right].isalpha() and text[right] != '': # checks if the character is not in the alphabet
            right -= 1 # skips character
            continue

        if text[left].lower() != text[right].lower() : # checks if both character does not match
            return False # this text is not a palindrome return False
        left += 1
        right -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    #Time: O(n)
    #Space: O(1)

    if text == '':
        return True

    if left is None and right is None:
        left, right = 0, len(text) - 1

    if left > right: # you successfully iterated through the text
        return True # text is a palindrome return True

    if not text[left].isalpha() and text[left] != '': # checks if the character is not a letter
        return is_palindrome_recursive(text, left + 1, right) # skip special character

    if not text[right].isalpha() and text[right] != '': # checks if the character is not a letter
        return is_palindrome_recursive(text, left, right - 1) # skip special character

    if text[left].lower() != text[right].lower(): # checks if both character does not match
        return False # this text is not a palindrome return False

    return is_palindrome_recursive(text, left + 1, right - 1)

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
