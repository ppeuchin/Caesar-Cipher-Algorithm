import sys
import time
from os import system, name

def decor(func):
    def wrap():
        print("[=======================================]")
        func()
        print("[=======================================]")
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