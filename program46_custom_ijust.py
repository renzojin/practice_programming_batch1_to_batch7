text = input("Enter a string: ")
width = int(input("Width: "))

if len(text) > width:
    spaces_needed = width - len(text)
    result = text + " " * spaces_needed
else:
    result = text

print(f"Original: {text}")
print(f"Result: {result}")
print(f"Length: {len(result)}")