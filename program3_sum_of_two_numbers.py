from colorama import Fore, Style, init
init(autoreset=True)

#Prog03: Print the sum
num1 = int(input(Fore.YELLOW + "Enter First Number: "))
num2 = int(input(Fore.YELLOW + "Enter Second Number: "))

print(num1 + num2)
print(" ")