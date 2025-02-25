def get_num_words(text: str):
    return len(text.split())

def get_chars_count(text: str):
    char_count = {}
    for char in text:
        c = char.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def chars_count_to_sorted_list(chars_count: dict):
    sorted_list = []
    for char in chars_count:
        sorted_list.append({ "char": char, "count": chars_count[char] })
    sorted_list.sort(reverse=True, key=lambda d: d["count"])
    return sorted_list
