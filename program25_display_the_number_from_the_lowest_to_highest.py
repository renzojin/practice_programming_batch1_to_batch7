numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)

    except ValueError:
        if numbers:
            numbers.sort()
            print("Numbers from lowest to highest are: ", numbers)
        else:
            print("Invalid input")
        break