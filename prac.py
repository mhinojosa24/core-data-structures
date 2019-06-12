def pattern_search(text: str, pattern: str):
    # text_len = len(text)
    # search_result = []
    # count = 0
    #
    # if len(pattern) == 0:
    #     return [index for index in range(len(text))]
    #
    #
    # for i in range(0, len(text)):
    #     window = len(pattern) + i
    #     # NOTE: early exit checks if the sliced index is less than
    #     print('window => ', text[i:window])
    #     print('pattern => ', len(pattern))
    #
    #     if len(text[i:window]) < len(pattern):
    #         return search_result
    #     print(pattern == text[i:window])
    #     if pattern == text[i:window]:
    #         search_result.append(i)
    #
    # return search_result
    txt_index = 0 # keeps track of each character position in text
    pat_index = 0 # keeps track of each character position in pattern
    result = []
    # time complexity: O(n) => goes through each character in string

    # edge case for empty string pattern
    if len(pattern) == 0:
        return [index for index in range(len(text))]

    while txt_index != len(text):
        if len(pattern) > 1: # checks if the pattern is greater than 2 characters
            if text[txt_index] == pattern[pat_index]: # checks if both characters match
                if pat_index == len(pattern) - 1: # checks if you went through the whole pattern
                    result.append(txt_index - pat_index) # successfully found a valid pattern add to array
                    pat_index = 0 # update index
                pat_index += 1 # update index
            else:
                txt_index -= pat_index # the beginning of found pattern index
                pat_index = 0
        elif text[txt_index] == pattern: # checks if both characters match
            result.append(txt_index) # save in array
        txt_index += 1 # update index
    return result

text = 'aaa'
pattern = 'a'
srt = 0
print(pattern_search(text, pattern))
