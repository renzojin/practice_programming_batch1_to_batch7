def custom_rjust(s, width, fillchar=' '):
    if len(s) >= width:
        return s

    spaces_needed = width - len(s)
    return fillchar * spaces_needed + s


text = "42"
print(f"Original: '{text}'")
print(f"rjust(5): '{custom_rjust(text, 5)}'")
print(f"rjust(5, '0'): '{custom_rjust(text, 5, '0')}'")