def find_pattern(text, pattern):
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

print(find_pattern('abc', 'z'))
