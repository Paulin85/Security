from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import hashlib
import cryptography
from cryptography.fernet import Fernet


def hacher_sel(algo, file):
    #Si l'algo choisi est blake2b alors :
    if (algo == "blake2b"):
        # création de l'objet du hachage en utilisant l'algorithme balke2b avec un sel pour obtenir un hash différent
        objet_hache = hashlib.blake2b(salt=b'16')
        file = open(file, 'rb')     # ouverture du fichier binaire en lecture afin de récupérer son contenu
        while True:
            blk = file.read(1024)   # Récupération de 1024 bits du fichier, le résultat sera stocké dans la variable blk
            if blk == b'': break    # fin du fichier c'est aussi la fin de la boucle.
        file.close()    # fermeture du fichier
        hache = objet_hache.hexdigest()# affichage du hache
    else :
        # création de l'objet du hachage en utilisant les différents algorithmes avec un sel pour obtenir un hash différent
        objet_hache = hashlib.pbkdf2_hmac(algo, b'password', b'salt', 100000)
        file = open(file, 'rb') # ouverture du fichier binaire en lecture afin de récupérer son contenu
        while True:
            blk = file.read(1024)   # Récupération de 1024 bits du fichier, le résultat sera stocké dans la variable blk
            if blk == b'': break    # fin du fichier c'est aussi la fin de la boucle.
        file.close()    # fermeture du fichier
        hache = objet_hache.hex()
    print(hache)# affichage du hache



def hachage(algo, file):
        # création de l'objet du hachage en utilisant les différents algorithmes
        objet_hache = hashlib.new(algo)
        file = open(file, 'rb')     # ouverture du fichier binaire en lecture afin de récupérer son contenu
        while True:
            blk = file.read(1024)   # Récupération de 1024 bits du fichier, le résultat sera stocké dans la variable blk
            if blk == b'': break    # fin du fichier c'est aussi la fin de la boucle.
        file.close()    # fermeture du fichier
        hache = objet_hache.hexdigest()
        print(hache)# affichage du hache




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



class Root(Tk):

    #declaration de l'interface et de tout ses objets
    def __init__(self):
        super(Root, self).__init__()
        self.title("Interface")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text="Ouvrir un fichier")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)
        self.label = ttk.Label(self, text="Le hachage sera affiché ici")
        self.label.grid(column=4, row=4, padx=20, pady=20)
        self.label2 = ttk.Label(self, text="Paulin SIROT / Mathias DATTIN")
        self.label2.grid(column=5, row=5, padx=20, pady=20)
        #self.fichier()
        self.choix()
        self.choix2()
        self.chiffrer()
        self.dechiffrer()

    #liste des algoritmes de hachage sans sel
    def choix(self):
        self.liste = Listbox()
        self.liste.insert(1, "SHA-1")
        self.liste.insert(2, "SHA-256")
        self.liste.insert(3, "SHA-512")
        self.liste.insert(4, "MD5")
        self.liste.insert(5, "blake2b")
        self.liste.grid(column=3, row=1)

    #liste des algoritmes de hachage avec sel
    def choix2(self):
        self.sel = Listbox()
        self.sel.insert(1, "SHA-1 - Sel")
        self.sel.insert(2, "SHA-256 - Sel")
        self.sel.insert(3, "SHA-512 - Sel")
        self.sel.insert(4, "MD5 - Sel")
        self.sel.insert(5, "blake2b - Sel")
        self.sel.grid(column = 4, row = 1)


    #fonction pour aller chercher le fichier à chiffrer
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Choisissez un fichier",
                                                   filetype=(("All Files", "*.*"), ("jpeg", "*.jpg") ))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text="Fichier chiffré")
        chiffrement(self.filename)

    #chiffrement du fichier
    def chiffrer(self):
        self.bouton = ttk.Button(self.labelFrame, text="Chiffrer", command=self.fileDialog)
        self.bouton.grid(column=5, row=1)



    #fonction pour aller chercher le fichier à déchiffrer
    def fileDialog2(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Choisissez un fichier",
                                                   filetype=(("All Files", "*.*"), ("jpeg", "*.jpg") ))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text="Fichier déchiffré")
        dechiffrement(self.filename)

    #déchiffrement du fichier
    def dechiffrer(self):
        self.bouton = ttk.Button(self.labelFrame, text="Déchiffrer", command=self.fileDialog2)
        self.bouton.grid(column=5, row=2)




if __name__ == '__main__':
    root = Root()
    root.mainloop()
