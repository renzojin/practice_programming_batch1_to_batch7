from colorama import Fore, Style, init
init(autoreset=True)

#Prog10: Print numbers 0–100 except ending in zero
for i in range(0,101):
    if i % 10 != 0:
        print(i)