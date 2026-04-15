text = input("Enter a string: ")

result = True
has_letter = False

for char in text:
    if "a" <= char <= "z":
        result = False
        break
    elif "A" <= char <= "Z":
        has_letter = True

if not has_letter:
    result = False