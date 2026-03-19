from colorama import Fore, Style, init
init(autoreset=True)

#Prog02: Print "Equal" when numbers are the same
num1 = int(input(Fore.CYAN + "Enter First Number: "))
num2 = int(input(Fore.CYAN + "Enter Second Number: "))

if num1 == num2:
    print("Equal")
print(" ")