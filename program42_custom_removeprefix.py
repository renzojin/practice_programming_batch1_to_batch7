text = input("Enter a string:")
prefix = input("Enter a prefix:")

if text[:len(prefix)] == prefix:
    result = text[len(prefix):]
else:
    result = text

print(f"Original: {text}")
print(f"Result: {result}")