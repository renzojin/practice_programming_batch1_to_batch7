text = input("Enter a string: ")
suffix = input("Enter a suffix: ")

if len(text) > len(suffix):
    result = text[-len(suffix):] == suffix
else:
    result = False
