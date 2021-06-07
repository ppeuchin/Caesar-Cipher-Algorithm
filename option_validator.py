from colorama.ansi import Fore, Style
from colours import print_with_color
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
        print_with_color("--------------------------", color=Fore.YELLOW, brightness=Style.BRIGHT)
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
        print_with_color("--------------------------", color=Fore.YELLOW, brightness=Style.BRIGHT)
        load_b()
        cd.caesar_decryption(ciphertext, key)

    elif option == '3':
        time.sleep(1.5)
        clear()
        print_with_color('[~~~~~~~~~~~~~~~~~~~~~~~~]',color=Fore.MAGENTA)
        time.sleep(1)
        print("  Thank you! :)")
        time.sleep(0.7)
        print("      See you next time!")
        time.sleep(0.5)
        sys.exit()

    else:
        time.sleep(1.5)
        print_with_color("Invalid Option.", color=Fore.RED)
        time.sleep(0.5)
        print_with_color("Try again!...", color=Fore.RED)
        print()
        time.sleep(1)
        options()