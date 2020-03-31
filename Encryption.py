import cryptography
from cryptography.fernet import Fernet


def chiffrement(fichier):
    # Generer une clé
    key = Fernet.generate_key()

    # Enregistrement de la clé dans le fichier key.key
    file = open('key.txt', 'wb')
    file.write(key)
    file.close()

    #Déclaration des fichiers d'entrée et de sortie
    input_file = fichier
    output_file = fichier+'.encrypted'
    with open(input_file, 'rb') as f:
        data = f.read() #insertion du contenu du fichier dans data

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data) #chiffrement de data grâce à la clé, dans la variable encrypted

    with open(output_file, 'wb') as f:
        f.write(encrypted) #remplacement du contenu du fichier par la variable encrypted



def dechiffrement(fichier):
    # Lecture du fichier key.txt
    file = open('key.txt', 'rb')
    key = file.read()   #récupération de la clé
    file.close()

    #déclaration des fichiers d'entrée et de sortie
    input_file = fichier
    output_file = fichier+'.txt'

    with open(input_file, 'rb') as f:
        data = f.read()     #insertion du contenu du fichier dans data

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)    #dechiffrement de data dans la variable decrypted

    with open(output_file, 'wb') as f:
        f.write(decrypted)      #le contenu du fichier devient la variable decrypted

