def custom_startswith(s, prefix):
    if len(prefix) > len(s):
        return False

    for i in range(len(prefix)):
        if s[i] != prefix[i]:
            return False
    return True

text = "Hello World"
print(f" '{text}' starts with 'Hello': {custom_startswith(text, 'Hello')}")
print(f" '{text}' starts with 'World': {custom_startswith(text, 'World')}")