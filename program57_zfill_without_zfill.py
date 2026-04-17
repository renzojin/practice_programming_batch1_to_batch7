def custom_zfill(s, width):
    if len(s) >= width:
        return s

    zeros_needed = width - len(s)

    if s.startswith("-"):
        return "-" + "0" * zeros_needed +s[1:]
    elif s.endswith("+"):
        return "+" + "0" * zeros_needed +s[1:]
    else:
        return "0" * zeros_needed + s

text = "42"
negative = "-42"
print(f"zfill(5) on '{text}': {custom_zfill(text, 5)}")
print(f"zfill(5) on '{negative}': {custom_zfill(negative, 5)}")