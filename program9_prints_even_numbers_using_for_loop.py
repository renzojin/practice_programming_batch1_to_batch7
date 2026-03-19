from colorama import Fore, Style, init
init(autoreset=True)

#Prog09: Print even numbers 0–100 using for loop
for i in range(0,101):
    if i % 2 == 0:
        print(i)

print(" ")