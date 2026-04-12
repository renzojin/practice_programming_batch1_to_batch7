numbers = []

while True:
    try:
        num = int(input("Enter the number: "))
        numbers.append(num)

    except ValueError:
        if numbers:
            lowest_number = min(numbers)
            print(lowest_number)
        else:
            print("Invalid input")
        break