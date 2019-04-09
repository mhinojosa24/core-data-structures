def is_palindrome_recursive(text, left=None, right=None):
    text = re.sub('[^A-Za-z0-9]+', '', text.lower())

    if left is None and right is None:
        left, right = 0, len(text) - 1


    if text[left] != text[right]:
        return False

    else:
        left += 1
        right -= 1
        return is_palindrome(text, left, right)
print(is_palindrome_recursive())
