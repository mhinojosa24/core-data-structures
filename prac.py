# def is_palindrome_recursive(text, left=None, right=None):
#     text = re.sub('[^A-Za-z0-9]+', '', text.lower())
#
#     if left is None and right is None:
#         left, right = 0, len(text) - 1
#
#
#     if text[left] != text[right]:
#         return False
#
#     else:
#         left += 1
#         right -= 1
#         return is_palindrome(text, left, right)
# print(is_palindrome_recursive())

# for blah in range(10):
#     print("iterated blah", blah)
#     if blah >= 3:
#         blah -= 1
#         print(blah)

# blah = 0
# while blah < 10:
#     if blah >= 3:
#         blah -= 1
#     blah += 1
#     print(blah)

# def find_index(text, pattern):
#     """Return the starting index of the first occurrence of pattern in text,
#     or None if not found."""
#     assert isinstance(text, str), 'text is not a string: {}'.format(text)
#     assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
#     # TODO: Implement find_index here (iteratively and/or recursively)
#     counter_main, counter_sub = 0, 0
#
#     if pattern == '' or text == pattern:
#         return 0
#
#     while counter_main < len(text):
#         print("main: ", counter_main)
#         if text[counter_main] == pattern[counter_sub]:
#             if counter_sub == len(pattern) - 1:
#                 return counter_main - counter_sub
#             counter_sub += 1
#         else:
#             counter_main -= counter_sub
#             counter_sub = 0
#         counter_main += 1
#
# print(find_index("", ""))
# print(find_index("bananas", "nas"))
# print(find_index("aaaaaag", "aaag"))


# def find_all_indexes(text, pattern):
#     counter_main = 0
#     counter_sub = 0
#     result = []
#     # print('init', counter_sub)
#     if pattern == '':
#         for index in range(len(text)):
#             result.append(index)
#         # print(result)
#
#     for index, letter in enumerate(text):
#         if text[index] == pattern:
#             result.append(index)
#     # print(result)
#
#     while counter_main != len(text):
#         # print('in while loop', counter_sub)
#         if text[counter_main] == pattern[counter_sub]:
#             # print('are they the same?', text[counter_main] == pattern[counter_sub])
#             # print('counter_sub same len of pattern?', counter_sub == len(pattern) - 1)
#             if counter_sub == len(pattern) - 1:
#                 quotent = counter_main - counter_sub
#                 result.append(quotent)
#             counter_sub += 1
#         else:
#             counter_main -= counter_sub
#             print('after else', counter_sub)
#             counter_sub = 0
#         counter_main += 1
#     return result

text = 'abc'
pattern = 'ab'
print(len(pa))
# print(find_all_indexes(text, pattern))
