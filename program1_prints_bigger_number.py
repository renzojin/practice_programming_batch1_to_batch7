from colorama import Fore, Style, init
init(autoreset=True)

#Program: Print the bigger number
num1 = int(input(Fore.CYAN + "Enter First Number: "))
num2 = int(input(Fore.CYAN + "Enter Second Number: "))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("Equal")

print(" ")