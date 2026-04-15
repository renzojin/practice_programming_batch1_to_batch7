text = input("Enter a string:")
width = int(input("Enter a width:"))

if len(text) < width:
    spaces_needed = width - len(text)
    left_spaces = spaces_needed // 2
    right_spaces = spaces_needed - left_spaces
    result = text[left_spaces:] + text[right_spaces:]
else:
    result = text

print(f"Original: {text}")
print(f"Result: {result}") 