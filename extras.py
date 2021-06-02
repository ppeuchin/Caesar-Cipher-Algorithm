import sys
import time

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
    print()

def load_b():
    for j in '..............':
        sys.stdout.write(j)
        sys.stdout.flush()
        time.sleep(0.3)
    print()

def load_c():
    for k in 'Almost there....':
        sys.stdout.write(k)
        sys.stdout.flush()
        time.sleep(0.3)
    print('\n')

def load_d():
    for i in 'Decrypting....':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.3)
    print()