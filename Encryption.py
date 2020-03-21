import cryptography
from cryptography.fernet import Fernet

#Generer une clé
key = Fernet.generate_key()

input_file='test.txt'
output_file = 'test.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

input_file = 'test.encrypted'
output_file = 'test.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)


# Enregistrement de la clé dans le fichier key.key
file = open('key.key', 'wb')
file.write(key)
file.close()

# Lecture du fichier key.key
file = open('key.key', 'rb')
key = file.read()
file.close()