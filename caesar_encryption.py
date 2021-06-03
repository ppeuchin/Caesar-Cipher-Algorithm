# Encryption algorithm
import time
from extras import decor

@decor
def intro():
    time.sleep(1)
    print("   Welcome To Caesar Cipher Encryptor")

def caesar_encryption(plaintext, key):
    encrypted_str = ""
 
    for i in plaintext:
        
        if i.isupper():
            uni_value = 65 + ((ord(i) - 65 + key) % 26)
            encrypted_str = encrypted_str + chr(uni_value)
        
        elif i.islower():
            uni_value = 97 + ((ord(i) - 97 + key) % 26)
            encrypted_str = encrypted_str + chr(uni_value)
        
        else:
            encrypted_str = encrypted_str + i
    
    time.sleep(1)
    print("The encrypted text is:", encrypted_str)