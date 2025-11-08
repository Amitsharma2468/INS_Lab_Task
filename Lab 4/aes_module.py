from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def generate_aes_key(bits):
    key = get_random_bytes(bits // 8)
    return key

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_aes_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ct_bytes

def decrypt_aes_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt.decode()

def encrypt_aes_cfb(plaintext, key):
    cipher = AES.new(key, AES.MODE_CFB)
    ct_bytes = cipher.encrypt(plaintext.encode())
    return cipher.iv + ct_bytes

def decrypt_aes_cfb(ciphertext, key):
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    pt = cipher.decrypt(ct)
    return pt.decode()
