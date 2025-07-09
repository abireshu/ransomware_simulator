import os
import base64
from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

password = b"gotit"
salt = os.urandom(16)

with open("salt.bin", "wb") as s:
    s.write(salt)

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)

key = base64.urlsafe_b64encode(kdf.derive(password))

with open("key.bin", "wb") as f:
    f.write(key)

print("Key and salt saved.")
