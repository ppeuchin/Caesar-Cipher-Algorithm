from colorama.ansi import Fore, Style
from colours import print_with_color
import time
from option_validator import options
from extras import clear

def redo():
    clear()
    print_with_color('*******************************', color=Fore.BLUE, brightness=Style.BRIGHT)
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