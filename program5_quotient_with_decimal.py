from colorama import Fore, Style, init
init(autoreset=True)

#Prog05: Print the quotient with decimal
num1 = int(input(Fore.YELLOW + "Enter First Number: "))
num2 = int(input(Fore.YELLOW + "Enter Second Number: "))

print(num1 / num2)
print(" ")