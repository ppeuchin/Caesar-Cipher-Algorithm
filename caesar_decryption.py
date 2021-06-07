# Decryption algorithm
from colorama.ansi import Fore
from colours import print_with_color
import time
from extras import decor

@decor
def intro():
    time.sleep(1)
    print_with_color("   Welcome To Caesar Cipher Decryptor", color=Fore.GREEN)

def note():
    print()
    print_with_color("NOTE: YOU ALWAYS NEED TO HAVE THE SAME KEY USED TO ENCRYPT THE TEXT!", color=Fore.RED)
    
def caesar_decryption(ciphertext, key):
    decrypted_str = ""

    for i in ciphertext:
        
        if i.isupper():
            
            if (ord(i) - 65 - key) < 0:
                uni_value = 65 + ((ord(i) - 65 - key) + 26) % 26
                decrypted_str = decrypted_str + chr(uni_value)
            
            else:
                uni_value = 65 + (ord(i) - 65 - key) % 26
                decrypted_str = decrypted_str + chr(uni_value)
        
        elif i.islower():
            
            if (ord(i) - 97 - key) < 0:
                uni_value = 97 + ((ord(i) - 97 - key) + 26) % 26
                decrypted_str = decrypted_str + chr(uni_value)
            
            else:
                uni_value = 97 + (ord(i) - 97 - key) % 26
                decrypted_str = decrypted_str + chr(uni_value)
        
        else:
            decrypted_str = decrypted_str + i
    
    time.sleep(1)
    print("The decrypted text is:", decrypted_str)