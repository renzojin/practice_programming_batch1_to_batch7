text = input("Enter a string with leading spaces: ")

i = 0
while i < len(text) and text[i] == ' ':
    i += 1

result = text[i:]
print(f"Original: {text}")
print(f"Result: {result}")