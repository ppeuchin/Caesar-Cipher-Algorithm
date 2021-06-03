# Caeser Cipher Encryption and Decryption Tool

from extras import decor
import time
from option_validator import options
from redo import redo

@decor
def display():
    print("        CAESAR CIPHER ALGORITHM")

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