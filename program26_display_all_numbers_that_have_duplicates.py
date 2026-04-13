numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

seen = set()
duplicate_numbers = []

for num in numbers:
    if num in seen:
        duplicate_numbers.append(num)

    else:
        seen.add(num)

if duplicate_numbers:
    print("Duplicate numbers:", sorted(duplicate_numbers))
else:
    print("No duplicate numbers")