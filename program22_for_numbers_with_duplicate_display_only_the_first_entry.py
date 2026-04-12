numbers = []

for i in range(10):
    num = int(input(f"Enter the number: "))
    numbers.append(num)

displayed = []
result = []

for num in numbers:
    if num not in displayed:
        displayed.appennd(num)
        result.append(num)

print("\nNumbers (duplicates shown only once):")
print(result)
