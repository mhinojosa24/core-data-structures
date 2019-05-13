import random



# def reorganize_word(word):
#     array = word.split(' ')
#     new_array = []
#
#     '''
#     checks each word if it contains ".", if so, remove the "." from word.
#     then randomly inserts each word in a different index.
#     '''
#     for word in array:
#         rand_int = random.randint(0, len(array))
#
#         if "." in word:
#             word = word[:-1] # removes the last character of index
#             # reversed_word = word[::-1] # reverse word
#             new_array.insert(rand_int, word)
#         else:
#             # reversed_word = word[::-1]
#             new_array.insert(rand_int, word)
#
#     sentence = ' '.join(new_array)
#
#
#
#     new_sentence = sentence[:1].upper() + sentence[1:]
#
#     return new_sentence

def rearrange_words(word):
    """
    A function that randomly rearranges a set of words provided as command-line arguments to the script
    """
    words = list(word)
    #     new_array = []
    # Run a loop that runs for how many elements in the list
    for w in range(0, len(words)):
        # pair random index with list
        rand_index = random.randint(0, len(words) -1)
        # word = words[w]
        # remove element from list
        word_taken_out = words.pop(rand_index)
        # add element to the end of the list
        words.append(word_taken_out)
        return ' '.join(words)


def is_in_dictionary(word):
    # new_word = reorganize_word(word)
    new_word = rearrange_words(word)
    with open('/usr/share/dict/words', 'r') as f:
        data = f.read().lower().split('\n')
        print(data[:5])

        while



def main():
    word = 'tefon'
    print(is_in_dictionary(word))

if __name__ == "__main__":
    main()
