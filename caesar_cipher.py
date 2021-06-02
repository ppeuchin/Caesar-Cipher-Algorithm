#Caeser Cipher Algorithm for encryption and decryption

import caesar_encryption, caesar_decryption
import time
import sys

def decor(func):
    def wrap():
        print("[=======================================]")
        func()
        print("\n[=======================================]")
    return wrap

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
    plaintext = input("Enter the text: ")
    key = int(input("Enter the key: "))
    
    for i in 'Encrypting....':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.3)
    print()

    for j in '..............':
        sys.stdout.write(j)
        sys.stdout.flush()
        time.sleep(0.3)
    print()

    for k in 'Almost there....':
        sys.stdout.write(k)
        sys.stdout.flush()
        time.sleep(0.3)
    print('\n')

    caesar_encryption.caesar_encryption(plaintext, key)

elif option == '2':
    ciphertext = input("Enter the encrypted text: ")
    key = int(input("Enter the key:"))
    caesar_decryption.caesar_decryption(ciphertext, key)

else:
    print("invalid option")