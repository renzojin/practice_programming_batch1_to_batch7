from operator import index


def custom_count(s, substring):
    if not substring:
        return len(s) + 1
    count = 0
    start = 0

    while True:
        index = s.find(substring, start)
        if index == -1:
            break
        count += 1
        start = index + 1

    return count

text = "hello hello hello world"
print(f"'{text}'")
print(f"Count of 'hello': {custom_count(text, 'hello')}")
print(f"Count of 'l': {custom_count(text, 'l')}")
