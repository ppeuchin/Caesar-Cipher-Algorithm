import time
from option_validator import options
import os

def redo():
    os.system('cls')
    print('*******************************')
    print('What would you like to do next?')
    time.sleep(1)
    print('\n1. Encrypt another')
    print('2. Decrypt another')
    print('3. Exit\n')
    time.sleep(1)
    options()
    print('\nPress any key to continue')
    input()
    redo()