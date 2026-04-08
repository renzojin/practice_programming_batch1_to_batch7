from colorama import Fore, Style, init
init(autoreset=True)

#Program: Prints the quotient without the decimal point.
num1 = int(input(Fore.CYAN + "Enter First Number: "))
num2 = int(input(Fore.CYAN + "Enter Second Number: "))

quotient = num1 // num2
print(quotient)