def custom_upper(s):
    result = []
    for char in s:
        if "a" <= char <= "z":
           result.append(chr(ord(char) - 32))
        else:
           result.append(char)
    return "".join(result)

text = "Hello World  "
print(f"Original: {text}")
print(f"Result: {custom_upper(text)}")