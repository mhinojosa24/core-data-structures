def search_string(text: str, pattern: str, starting_point: int = 0) -> int:
    text_len = len(text)

    for i in range(starting_point, len(text)):
        if pattern[0] == text[i]:
            window = len(pattern) + 1
            
            if window > text_len:
                return -1

            if pattern == text[i:window]:
                return i
    return -1


text = 'aagaaaagag'
pattern = 'aaag'
srt = 0
print(search_string(text, pattern, srt))
