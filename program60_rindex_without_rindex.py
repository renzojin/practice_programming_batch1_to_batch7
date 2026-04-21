def custom_rindex(s, substring, start=0, end=None):
    if end is None:
        end = len(s)

    sub_len = len(substring)
    for i in range(end - sub_len, start - 1, -1):
        if s[i:i + sub_len] == substring:
            return i

    raise ValueError(f"substring '{substring}' not found")

text = "hello hello world"
try:
    print(f"'{text}'")
    print(f"Last index of 'hello': {custom_rindex(text, 'hello')}")
    print(f"Last index of 'l': {custom_rindex(text, 'l')}")
    print(f"Last index of 'xyz': {custom_rindex(text, 'xyz')}")
except ValueError as e:
    print(f"Error: {e}")