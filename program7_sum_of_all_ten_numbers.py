from colorama import Fore, Style, init
init(autoreset=True)

#Prog07: Sum of 10 numbers
total = 0
for i in range(10):
    n = int(input(Fore.YELLOW + "Enter number: "))
    total += n

print(total)
print(" ")