def custom_rstrip(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    return s[:i+1]

text = "Hello World  "
print(f"Original: {text}")
print(f"Result: {custom_rstrip(text)}")