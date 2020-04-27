# Uses PBKDF2 Hash. Requires passlib
# Install with pip install passlib

import os, hashlib

def hashThis(inputPassword):
    salt = os.urandom(32)

    key = hashlib.pbkdf2_hmac('sha256', inputPassword.encode("ascii"), salt, 100000, dklen=128)
    return 

# print(a.decode("utf-8"))

# def checkThis(inputPassword, salt):
#     key = hashlib.pbkdf2_hmac('sha256', inputPassword, salt, 100000, dklen=128)
#     return key, salt

# c = checkThis(inp.encode("utf-8"), b)

# print(a == c)

