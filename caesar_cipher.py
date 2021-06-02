#Caeser Cipher Algorithm for Encryption and Decryption

from caesar_encryption import caesar_encryption, intro
from caesar_decryption import caesar_decryption
from extras import decor, load_a, load_b, load_c, load_d
import time

@decor
def display():
    print("        CAESAR CIPHER ALGORITHM")

display()

time.sleep(0.5)

print("Hello there! What can i help you with?")
time.sleep(1)
print("\n1. Encryption")
time.sleep(0.3)
print("2. Decryption\n")
time.sleep(1)

option = input("Input an option: ")

if option == '1':
    time.sleep(1.5)
    intro()
    print()
    time.sleep(1)
    plaintext = input("Enter the text: ")
    time.sleep(0.5)
    key = int(input("Enter the key: "))
    time.sleep(1)
    print("--------------------------")
    load_a()
    load_b()
    load_c()
    caesar_encryption(plaintext, key)

elif option == '2':
    time.sleep(1.5)
    intro()
    print()
    time.sleep(1)
    ciphertext = input("Enter the encrypted text: ")
    time.sleep(0.5)
    key = int(input("Enter the key:"))
    time.sleep(1)
    print("--------------------------")
    load_d()
    load_b()
    load_c()
    caesar_decryption(ciphertext, key)

else:
    time.sleep(1.5)
    print()
    print("invalid option")