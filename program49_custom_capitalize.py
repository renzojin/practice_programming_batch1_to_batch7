text = input("Enter a string: ")

if text:
    first_char = text[0]
    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)

    rest = ""
    for char in text[1:]:
        if 'A' <= char <= 'Z':
            rest += chr(ord(char) + 32)
        else:
            rest += char
    result = first_char + rest
else:
    result = ""

print(f"Original: '{text}'")
print(f"Result: '{result}'")