import base64
from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

with open("salt.bin", "rb") as s:
    salt = s.read()

password = b"gotit"

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))

f = Fernet(key)

filename = "testing\open.txt" 

with open(filename, "rb") as file:
    original_data = file.read()

encrypted_data = f.encrypt(original_data)

with open(filename, "wb") as file:
    file.write(encrypted_data)
print("encrypted successfully")
