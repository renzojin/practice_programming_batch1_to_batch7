numbers = []

for i in range(10):
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input")
        break

if numbers:
    print("The highest number is: ", max(numbers))
else:
    print("No valid input.")