import time
import sys
from extras import load_a, load_b,clear
import caesar_encryption as ce
import caesar_decryption as cd

def options():
    option = input("Input an option: ")
    print()
    if option == '1':
        time.sleep(1.5)
        clear()
        ce.intro()
        ce.note()
        print()
        time.sleep(1)
        plaintext = input("Enter the text: ")
        time.sleep(0.5)
        key = int(input("Enter the key: "))
        print()
        time.sleep(1)
        print("--------------------------")
        load_a()
        ce.caesar_encryption(plaintext, key)

    elif option == '2':
        time.sleep(1.5)
        clear()
        cd.intro()
        cd.note()
        print()
        time.sleep(1)
        ciphertext = input("Enter the encrypted text: ")
        time.sleep(0.5)
        key = int(input("Enter the key: "))
        print()
        time.sleep(1)
        print("--------------------------")
        load_b()
        cd.caesar_decryption(ciphertext, key)

    elif option == '3':
        time.sleep(1.5)
        clear()
        msg = "Thank you! :)\nSee you next time!"
        sys.exit(msg)

    else:
        time.sleep(1.5)
        print("Invalid Option.")
        time.sleep(0.5)
        print("Try again!...")
        print()
        time.sleep(1)
        options()