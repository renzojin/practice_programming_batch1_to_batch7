def custom_removesuffix(s, suffix):
    if s.endswith(suffix):
        return s[:-len(suffix)]
    return s

text = "Hello World  "
print(f"Original: {text}")
print(f"Result: {custom_removesuffix(text,'.py')}" )