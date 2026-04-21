def custom_index(s, substring, start=0, end=None):
    if end is None:
        end = len(s)

    # Search for substring
    sub_len = len(substring)
    for i in range(start, end - sub_len + 1):
        if s[i:i + sub_len] == substring:
            return i

    raise ValueError(f"substring '{substring}' not found")

text = "Hello World"
try:
    print(f"'{text}'")
    print(f"Index of 'World': {custom_index(text, 'World')}")
    print(f"Index of 'l': {custom_index(text, 'l')}")
    print(f"Index of 'xyz': {custom_index(text, 'xyz')}")
except ValueError as e:
    print(f"Error: {e}")