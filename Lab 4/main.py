import os, time
from aes_module import *
from rsa_module import *
from hash_module import *
from benchmark import benchmark_aes, benchmark_rsa

for folder in ['keys', 'encrypted_files', 'decrypted_files', 'signatures']:
    if not os.path.exists(folder):
        os.makedirs(folder)

def aes_flow():
    bits = int(input("AES key size (128/256): "))
    mode = input("Mode (ECB/CFB): ").upper()
    key_file = f'keys/aes_key_{bits}.key'
    key = generate_aes_key(bits) if not os.path.exists(key_file) else load_key(key_file)
    if not os.path.exists(key_file): save_key(key, key_file)
    text = input("Enter text to encrypt: ")

    start = time.time()
    if mode=='ECB':
        ct = encrypt_aes_ecb(text,key)
        pt = decrypt_aes_ecb(ct,key)
        enc_file = 'encrypted_files/aes_ecb.enc'
        dec_file = 'decrypted_files/aes_ecb_decrypted.txt'
    else:
        ct = encrypt_aes_cfb(text,key)
        pt = decrypt_aes_cfb(ct,key)
        enc_file = 'encrypted_files/aes_cfb.enc'
        dec_file = 'decrypted_files/aes_cfb_decrypted.txt'

    with open(enc_file,'wb') as f: f.write(ct)
    with open(dec_file,'w', encoding='utf-8') as f: f.write(pt)
    end = time.time()
    print(f"Encrypted file: {enc_file}\nDecrypted file: {dec_file}\nTime: {end-start:.6f} sec")

def rsa_flow():
    priv_file, pub_file = 'keys/rsa_private.pem','keys/rsa_public.pem'
    if not os.path.exists(priv_file):
        priv, pub = generate_rsa_key(2048)
        save_key(priv, priv_file)
        save_key(pub, pub_file)
    priv, pub = load_key(priv_file), load_key(pub_file)
    text = input("Enter text for RSA: ")

    start=time.time()
    ct=encrypt_rsa(text,pub)
    pt=decrypt_rsa(ct,priv)
    enc_file='encrypted_files/rsa.enc'
    dec_file='decrypted_files/rsa_decrypted.txt'

    with open(enc_file,'wb') as f: f.write(ct)
    with open(dec_file,'w', encoding='utf-8') as f: f.write(pt)
    end=time.time()
    print(f"Encrypted file: {enc_file}\nDecrypted file: {dec_file}\nTime: {end-start:.6f} sec")

    # Signature
    start=time.time()
    sig=sign_rsa(text,priv)
    sig_file='signatures/rsa.sig'
    with open(sig_file,'wb') as f: f.write(sig)
    verified=verify_rsa(text,sig,pub)
    end=time.time()
    print(f"Signature file: {sig_file}\nVerified: {verified}\nTime: {end-start:.6f} sec")

def sha_flow():
    file=input("Enter file path to hash: ")
    start=time.time()
    digest=hash_sha256(file)
    end=time.time()
    print(f"SHA-256: {digest}\nTime: {end-start:.6f} sec")

def benchmark_flow():
    print("Running AES benchmark...")
    benchmark_aes()
    print("Running RSA benchmark...")
    benchmark_rsa()

def main():
    while True:
        print("\nMenu:\n1.AES\n2.RSA\n3.SHA-256\n4.Benchmark\n5.Exit")
        choice=input("Choice: ")
        [aes_flow,rsa_flow,sha_flow,benchmark_flow][int(choice)-1]() if choice in '1234' else exit()

if __name__=="__main__":
    main()
