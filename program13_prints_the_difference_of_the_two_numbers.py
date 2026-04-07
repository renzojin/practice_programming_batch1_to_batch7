from colorama import Fore, Style, init
init(autoreset=True)

#Program: Prints the difference.
num1 = int(input(Fore.CYAN + "Enter First Number: "))
num2 = int(input(Fore.CYAN + "Enter Second Number: "))

difference = num1 - num2
print(difference)