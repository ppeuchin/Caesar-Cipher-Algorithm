import time
import os
from extras import load_a, load_b, load_c, load_d
import caesar_encryption as ce
import caesar_decryption as cd

def options():
    option = input("Input an option: ")
    print()
    if option == '1':
        time.sleep(1.5)
        os.system('cls')
        ce.intro()
        print()
        time.sleep(1)
        plaintext = input("Enter the text: ")
        time.sleep(0.5)
        key = int(input("Enter the key: "))
        print()
        time.sleep(1)
        print("--------------------------")
        load_a()
        load_b()
        load_c()
        ce.caesar_encryption(plaintext, key)

    elif option == '2':
        time.sleep(1.5)
        os.system('cls')
        cd.intro()
        print()
        time.sleep(1)
        ciphertext = input("Enter the encrypted text: ")
        time.sleep(0.5)
        key = int(input("Enter the key: "))
        print()
        time.sleep(1)
        print("--------------------------")
        load_d()
        load_b()
        load_c()
        cd.caesar_decryption(ciphertext, key)

    else:
        time.sleep(1.5)
        print("Invalid Option.")
        time.sleep(0.5)
        print("Try again!...")
        print()
        time.sleep(1)
        options()