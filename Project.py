import hashlib
import cryptography
from cryptography.fernet import Fernet


def hacher_sel(algo, file):
    if (algo == "blake2b"):
        objet_hache = hashlib.blake2b(salt=b'16')
        file = open(file, 'rb')
        while True:
            blk = file.read(1024)
            if blk == b'': break
        file.close()
        hache = objet_hache.hexdigest()
    else :
        objet_hache = hashlib.pbkdf2_hmac(algo, b'password', b'salt', 100000)
        file = open(file, 'rb')
        while True:
            blk = file.read(1024)
            if blk == b'': break
        file.close()
        hache = objet_hache.hex()
    print(hache)

def hacher(algo, file):
        objet_hache = hashlib.new(algo)
        file = open(file, 'rb')
        while True:
            blk = file.read(1024)
            if blk == b'': break
        file.close()
        hache = objet_hache.hexdigest()
        print(hache)

#Generer une clé
key = Fernet.generate_key()

def chiffrer(file):
    # Generer une clé
    input_file = file
    output_file = file+'.encrypted'
    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)

def dechiffrer(file):
    input_file = file
    output_file = file+'.txt'

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)



hacher("blake2b", "test2.txt")
hacher_sel("blake2b", "test2.txt")
chiffrer("test2.txt")
dechiffrer("test2.txt.encrypted")