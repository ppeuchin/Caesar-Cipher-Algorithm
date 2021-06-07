# Caeser Cipher Encryption and Decryption Tool

from colorama.ansi import Fore
from extras import decor
import time
from option_validator import options
from redo import redo
from colours import print_with_color

time.sleep(1)
@decor
def display():
    print_with_color("        CAESAR CIPHER ALGORITHM", color=Fore.BLUE)

display()

time.sleep(0.5)

print()
print("Hello there! What can i help you with?")
time.sleep(1)
print("\n1. Encryption")
print("2. Decryption")
print("3. Exit\n")
time.sleep(1)

options()
print('\nPress any key to continue')
input()
redo()