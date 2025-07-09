import base64
import getpass
import os

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

filename = r"testing\\open.txt"


try:
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")

except Exception as e:
    print(f" Failed to decrypt: {e}")
#os.startfile(filename)