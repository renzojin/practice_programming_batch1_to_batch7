from collections import Counter

numbers = []
for i in range(10):
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input")
        break

if numbers:
    count_dict = Counter(numbers)
    max_count = max(count_dict.values())
    most_frequent = [num for num, count in count_dict.items() if count == max_count]

    print(f"\nNumbers entered: {numbers}")
    print(f"Most frequent number(s): {most_frequent}")
    print(f"Appears {max_count} time(s)")
else:
    print("No numbers found")