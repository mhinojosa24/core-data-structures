def is_palindrome_recursive(text, left=None, right=None):
    if text == '':
        return True

    if left is None and right is None:
        left, right = 0, len(text) - 1

    if not text[left].isalpha() and not text[right] == '': # checks if the character is not a letter
        left += 1 # skip special character

    if not text[right].isalpha() and not text[right] == '': # checks if the character is not a letter
        print(text[right])
        right -= 1 # skip special character
        print('hi')

    if text[left].lower() != text[right].lower():
        print('left index: {}, right index: {}'.format(text[left], text[right]))
        return False

    else:
        left += 1
        right -= 1
        if left > right:
            return True
        return is_palindrome_recursive(text, left, right)


# print(is_palindrome_recursive('Bb'))
print(is_palindrome_recursive('no, on!'))


text = 'no, on!'
