# Uses PBKDF2 Hash. Requires passlib
# Install with pip install passlib

import os, hashlib

def hashThis(inputPassword):
    salt = os.urandom(32)

    key = hashlib.pbkdf2_hmac('sha256', inputPassword.encode("ascii"), salt, 100000, dklen=128)
    return 
