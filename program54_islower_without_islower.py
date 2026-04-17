def custom_islower(s):
    if not s:
        return False

    has_letter = False
    for char in s:
        if "A" <= char <= "Z":
            return False
        if "a" <= char <= "z":
            has_letter = True

    return has_letter

first_text = "hello"
second_text = "Hello"
third_text = "123"
print(f"Original: {custom_islower(first_text)}")
print(f"Result: {custom_islower(second_text)}")
print(f"Result: {custom_islower(third_text)}")