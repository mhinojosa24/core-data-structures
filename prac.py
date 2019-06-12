def search_string(text: str, pattern: str, starting_point: int = 0) -> int:
    text_len = len(text)
    arr = []
    count = 0
    for i in range(starting_point, len(text)):
        window = len(pattern) + i
        # NOTE: early exit checks if the sliced index is less than
        if len(text[i:window]) < len(pattern):
            return False
        if pattern == text[i:window]:
            return i
    return False



text = 'caabra'
pattern = 'a'
srt = 0
print(search_string(text, pattern, srt))
