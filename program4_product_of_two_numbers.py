from colorama import Fore, Style, init
init(autoreset=True)

#Prog04: Print the product
num1 = int(input(Fore.CYAN + "Enter First Number: "))
num2 = int(input(Fore.CYAN + "Enter Second Number: "))

print(num1 * num2)
print(" ")