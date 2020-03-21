# Programme Python qui affiche le hachage d'un fichier

# import hashlib module
import hashlib

# création de l'objet du hachage en utilisant les différents algorithmes
#objet_hash_sha2562 = hashlib.sha256()
#objet_hash_md5 = hashlib.md5()
#objet_hash_blake2b = hashlib.blake2b()
#objet_hash_sha1 = hashlib.sha1()
#objet_hash_sha512 = hashlib.sha512()

def hacher(algo, file):
    objet_hache = hashlib.pbkdf2_hmac(algo, b'password', b'salt', 100000)
    file = open(file, 'rb')
    while True:
        blk = file.read(1024)
        if blk == b'': break
    file.close()
    hache = objet_hache.hex()
    print(hache)


# création de l'objet du hachage en utilisant les différents algorithmes avec un salt pour obtenir un hash différent
objet_hash_sha256 = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
objet_hash_md5 = hashlib.pbkdf2_hmac('md5', b'password', b'salt', 100000)
objet_hash_blake2b = hashlib.blake2b(salt=b'salt')
objet_hash_sha1 = hashlib.pbkdf2_hmac('sha1', b'password', b'salt', 100000)
objet_hash_sha512 = hashlib.pbkdf2_hmac('sha512', b'password', b'salt', 100000)



# ouverture du fichier binaire en lecture afin de récupérer son contenu
file = open('JulesVerne-VoyageaucentredelaTerre.epub', 'rb')

while True:  # boucle toujours ouverte

    # Récupération de 1024 bits du fichier, le résultat sera stocké dans la variable blk
    blk = file.read(1024)



    # Mettez à jour l'objet de hachage objet_hash avec la chaîne blk.
    # Les appels répétés sont équivalents à un seul appel avec la concaténation de tous les arguments:
    # objet_hash.update(a); objet_hash.update(b) est équivalent à objet_hash.update(a + b).
    # objet_hash.update(blk.encode()) s'il s'agit d'un fichier texte

    #objet_hash_sha256.update(blk)
    #objet_hash_md5.update(blk)
    #objet_hash_blake2b.update(blk)
    #objet_hash_sha1.update(blk)
    #objet_hash_sha512.update(blk)

    if blk == b'': break  # fin du fichier c'est aussi la fin de la boucle.

file.close()  # fermeture du fichier

message_hache_sha256 = objet_hash_sha256.hex()
message_hache_md5 = objet_hash_md5.hex()
message_hache_blake2b = objet_hash_blake2b.hexdigest()
message_hache_sha1 = objet_hash_sha1.hex()
message_hache_sha512 = objet_hash_sha512.hex()


# affichage du message
#print(message_hache_sha256)
#print(message_hache_md5)
#print(message_hache_blake2b)
#print(message_hache_sha1)
#print(message_hache_sha512)

hacher("md5", "test.txt")