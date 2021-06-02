#Caeser Cipher Algorithm for encryption and decryption

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
    
    print("The encrypted text is:", encrypted_str)

plaintext = input("Enter the text: ")
key = int(input("Enter the key: "))
caesar_encryption(plaintext, key)

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

    print("The decrypted text is:", decrypted_str)       

ciphertext = input("Enter the encrypted text: ")
key = int(input("Enter the key:"))
caesar_decryption(ciphertext, key) 