def get_num_words(text):
    separate = text.split()
    return len(separate)

# -----------------------------------

def get_num_char(text) -> dict[str, int]:
    counts: dict[str, int] = {}
    lower = text.lower()
    for char in lower:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

# -----------------------------------

def sort_on_num(item):
    return item["num"]

# -----------------------------------

def sort_in_order(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char" : char, "num":count})
    char_list.sort(reverse=True, key=sort_on_num)
    return char_list

# -----------------------------------
