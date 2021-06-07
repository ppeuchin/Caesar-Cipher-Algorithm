from colorama.ansi import Fore
from colours import print_with_color
import sys
import time
from os import system, name

def decor(func):
    def wrap():
        print_with_color("[=======================================]", color=Fore.CYAN)
        func()
        print_with_color("[=======================================]", color=Fore.CYAN)
    return wrap

def load_a():
    for i in 'Encrypting....':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.3)
    print('\n')

def load_b():
    for i in 'Decrypting....':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.3)
    print('\n')

def clear():
    # Windows
    if name == 'nt':
        system('cls')
    # Mac and Linux
    else:
        system('clear')