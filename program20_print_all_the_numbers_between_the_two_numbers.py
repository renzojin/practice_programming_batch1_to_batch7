from colorama import Fore, Style, init
init(autoreset=True)

num1 = int(input(Fore.CYAN + "Enter first number: "))
num2 = int(input(Fore.CYAN + "Enter second number: "))

start = min(num1, num2) +1
end = max(num1, num2)

if start <= end:
    for num in range(start, end):
        print(num, end=" ")
else:
    print("No numbers between the two numbers.")

print(" ")