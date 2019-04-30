from linkedlist import LinkedList


def redact_words(words, banned_words):
    word_list = [LinkedList() for word in words]

    for word in banned_words:


words = ['A', 'B', 'C', 'D', 'E']
banned_words = ['B', 'D', 'E']
print(redact_words(words, banned_words))
