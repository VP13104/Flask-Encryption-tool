from flask import jsonify
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os 
import base64
import hashlib


# normalize key
def normalize_key(key):
    return hashlib.sha256(key.encode('utf-8')).digest()

# iv generation 
aes_iv = os.urandom(16)

def encrypt(plaintext, key):
    key_bytes = normalize_key(key)

    # pad plaintext to block size 
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
    
    #AES-CBC Encryption 
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(aes_iv), backend=default_backend())
    encryptor = cipher.encryptor()
    cipertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # return Base64 data 
    result = {
        "ciphertext": base64.b64encode(cipertext).decode(),
        "iv": base64.b64encode(aes_iv).decode()
    }
    return result 
 

def decrypt(ciphertext, key, iv):
   key_bytes = normalize_key(key)
   ciphertext = base64.b64decode(ciphertext)
   iv = base64.b64decode(iv)
   
   #AES-CBC Decryption
   cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
   decryptor = cipher.decryptor()
   padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

   unpadder = padding.PKCS7(128).unpadder()
   plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

   return plaintext.decode()
