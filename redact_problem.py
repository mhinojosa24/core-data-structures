from linkedlist import LinkedList


def redact_words(words, banned_words):
    word_list = LinkedList(words)


    for word in banned_words:
        found_word = word_list.find(lambda werd: werd == word)
        if found_word is not None:
            word_list.delete(found_word)
    return word_list
words = ['A', 'B', 'C', 'D', 'E']
banned_words = ['B', 'D', 'E']
print(redact_words(words, banned_words))
