from colorama import Fore, Style, init
init(autoreset=True)

#Program: Prints "Not Equal." when numbers are not the same.
num1 = int(input(Fore.CYAN + "Enter First Number: "))
num2 = int(input(Fore.CYAN + "Enter Second Number: "))

if num1 != num2:
    print("Not Equal.")
