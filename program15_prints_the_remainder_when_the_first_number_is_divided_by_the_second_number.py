from colorama import Fore, Style, init
init(autoreset=True)

num1 = int(input(Fore.CYAN + "Enter the First number: "))
num2 = int(input(Fore.CYAN + "Enter the Second number: "))

remainder = num1 % num2
print(remainder)