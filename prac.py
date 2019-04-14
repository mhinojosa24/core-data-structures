# text = 'aaaaaag'
# pattern = 'aaag'
# result = []
#
# txt_index = 0
# pat_index = 0
#
# if len(pattern) == 0:
#     return [index for index in range(len(text))]:
#
# for index, letter in enumerate(text):
#     if text[index] == pattern:
#         result.append(index)
#     if text[index] == pattern[pat_index]:
#         if pat_index == len(pattern) - 1:
#             result.append(index - pat_index)
#         pat_index += 1
#     else:
#         index -= pat_index
#
#
# while txt_index != len(text):
#     if text[txt_index] == pattern[pat_index]:
#         if pat_index == len(pattern) - 1:
#             result.append(txt_index - pat_index)
#         pat_index += 1
#     else:
#         txt_index -= pat_index
#         pat_index = 0
#     txt_index += 1
# print(result)



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    txt_index = 0 # keeps track of each character position in text
    pat_index = 0 # keeps track of each character position in pattern
    result = []

    # edge case for empty string pattern
    if len(pattern) == 0:
        result.append(index for index in range(len(text)))
    num = 0
    while txt_index != len(text):
        num += 1
        if len(pattern) > 1:
            if text[txt_index] == pattern[pat_index]:
                # print('before found', pat_index)
                # print(txt_index)
                # print(pat_index)
                print(pat_index == len(pattern))
                if pat_index == len(pattern) - 1:
                    print('after found pattern', pat_index)
                    result.append(txt_index - pat_index)
                pat_index += 1
                print(pat_index)
            else:
                # print('hi')
                txt_index -= pat_index
                pat_index = 0
            txt_index += 1
        elif text[txt_index] == pattern:
            result.append(txt_index)
        txt_index += 1
    return result


# text = 'aaaaaag'
# pattern = 'aaag'
text = 'ababc'
pattern = 'ab'
print(find_all_indexes(text, pattern))
