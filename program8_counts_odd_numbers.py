from colorama import Fore, Style, init
init(autoreset=True)

#Prog08: Count odd numbers from 10 inputs
count = 0
for i in range(10):
    n = int(input(Fore.CYAN + "Enter number: "))
    if n % 2 != 0:
        count += 1

print(count)
print(" ")