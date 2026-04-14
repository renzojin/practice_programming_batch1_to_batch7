full_name = input("Enter full name (incorrect casing): ")
snake_case = '_'.join(word.lower() for word in full_name.split())
print(snake_case)
