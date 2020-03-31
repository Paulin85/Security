# Programme Python qui affiche le hachage d'un fichier

# import hashlib module
import hashlib

import sys


def hacher_sel(algo, file):
    #Si l'algo choisi est blake2b alors :
    if (algo == "blake2b"):
        # création de l'objet du hachage en utilisant l'algorithme balke2b avec un sel pour obtenir un hash différent
        objet_hache = hashlib.blake2b(salt=b'16')
        file = open(file, 'rb')     # ouverture du fichier binaire en lecture afin de récupérer son contenu
        while True:
            blk = file.read(1024)   # Récupération de 1024 bits du fichier, le résultat sera stocké dans la variable blk
            if blk == b'': break
            objet_hache.update(blk)
            # fin du fichier c'est aussi la fin de la boucle.
        file.close()    # fermeture du fichier
        hache = objet_hache.hexdigest()# affichage du hache
    else :
        # création de l'objet du hachage en utilisant les différents algorithmes avec un sel pour obtenir un hash différent
        objet_hache = hashlib.pbkdf2_hmac(algo, b'password', b'', 100000)
        file = open(file, 'rb') # ouverture du fichier binaire en lecture afin de récupérer son contenu
        while True:
            blk = file.read(1024)   # Récupération de 1024 bits du fichier, le résultat sera stocké dans la variable blk
            if blk == b'': break
            # fin du fichier c'est aussi la fin de la boucle.
        file.close()    # fermeture du fichier
        hache = objet_hache.hex()
    print(hache)# affichage du hache



def hachage(algo, file):
        # création de l'objet du hachage en utilisant les différents algorithmes
        objet_hache = hashlib.new(algo)
        file = open(file, 'rb')     # ouverture du fichier binaire en lecture afin de récupérer son contenu
        while True:
            blk = file.read(1024)   # Récupération de 1024 bits du fichier, le résultat sera stocké dans la variable blk
            if blk == b'': break
            objet_hache.update(blk)
            # fin du fichier c'est aussi la fin de la boucle.
        file.close()    # fermeture du fichier

        hache = objet_hache.hexdigest()
        print(hache)# affichage du hache

hachage(sys.argv[1], sys.argv[2])
hacher_sel(sys.argv[1], sys.argv[2])