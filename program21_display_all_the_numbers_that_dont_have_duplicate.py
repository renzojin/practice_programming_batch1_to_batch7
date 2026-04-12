numbers = []

for i in range(10):
    num = int(input(f"Enter the number: "))
    numbers.append(num)

unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

print("\n Unique numbers:")
print(unique_numbers)
