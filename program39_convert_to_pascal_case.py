full_name = input("Enter full name (incorrect casing): ")
pascal_case = ''.join(word.capitalize() for word in full_name.split())
print(pascal_case)