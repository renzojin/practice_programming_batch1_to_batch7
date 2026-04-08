from colorama import Fore, Style, init
init(autoreset=True)

numbers = []
for i in range(10):
    num = float(input(Fore.CYAN + "Enter number {i+1}: "))
    numbers.append(num)

result = numbers[0]
for i in range(1, 10):
    result -= numbers[i]

print(result)