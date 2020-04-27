# PBKDF2 HASH memakai hashlib

import hashlib, binascii, os # Digunakan untuk generate angka random

def hashPassword(password):
    # Membuat salt berdasarkan nomor random yang diubah menjadi ASCII
    salt = hashlib.sha256(os.urandom(32)).hexdigest().encode('ascii')

    # Hash password dengan PBKDF2
    key = hashlib.pbkdf2_hmac("sha512", password.encode('ascii'), salt, 100000)

    # Mengubah hash menjadi bentuk hexadesimal
    key = binascii.hexlify(key) 

    # Memberi output password yang sudah dihash dan saltnya dalam ASCII
    return (salt + key).decode('ascii')

def verifyPassword(password, inputPass):

    # Salt
    salt = password[:64]

    # Menghilangkan salt dari password
    password = password[64:]

    # Hash input password. 
    hashedInput = hashlib.pbkdf2_hmac('sha512', inputPass.encode('ascii'), salt.encode('ascii'), 100000) 

    # Mengubah hashed input menjadi benduk hexadesimal
    hashedInput = binascii.hexlify(hashedInput).decode('ascii') 

    return password == hashedInput
