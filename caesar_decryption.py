#Decryption algorithm
import time
#import sys
from extras import decor

@decor
def intro():
    time.sleep(1)
    print("   Welcome To Caesar Cipher Decryptor")

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

    # for i in decrypted_str:
    #     sys.stdout.write(i)
    #     sys.stdout.flush()
    #     time.sleep(0.2)