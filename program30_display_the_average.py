numbers = []

for i in range(10):
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input.")
        break

if numbers:
    average = sum(numbers) / len(numbers)
    print("The average is: ", average)
else:
    print("No valid input.")
