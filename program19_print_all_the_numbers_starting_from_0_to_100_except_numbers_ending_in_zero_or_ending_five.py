# Print all numbers from 0 to 100 except numbers ending in 0 or 5
for num in range(0, 101):
    last_digit = num % 10
    if last_digit != 0 and last_digit != 5:
        print(num, end=" ")

print()