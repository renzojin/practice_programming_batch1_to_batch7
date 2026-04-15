text = input("Enter a string: ")

result = ""
for char in text:
    if "A" <= char <= "Z":
        result += chr(ord(char) + 32)
    else:
        result += char

print(f"Original: {text}")
print(f"Result: {result}")