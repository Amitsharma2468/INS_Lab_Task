import time
import matplotlib.pyplot as plt
from aes_module import *
from rsa_module import *

def benchmark_aes():
    aes_sizes = [128, 192, 256]  # Correct AES key sizes in bits
    modes = ['ECB', 'CFB']
    results = {mode: [] for mode in modes}
    sample_text = "AES timing benchmark sample text."

    for size in aes_sizes:
        key = generate_aes_key(size)
        for mode in modes:
            start = time.time()
            if mode == 'ECB':
                ct = encrypt_aes_ecb(sample_text, key)
                pt = decrypt_aes_ecb(ct, key)
            else:
                ct = encrypt_aes_cfb(sample_text, key)
                pt = decrypt_aes_cfb(ct, key)
            end = time.time()
            results[mode].append(end - start)

    plt.figure()
    for mode in modes:
        plt.plot(aes_sizes, results[mode], marker='o', label=f"AES {mode}")
    plt.title("AES Encryption/Decryption Execution Time")
    plt.xlabel("Key Size (bits)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig("AES_benchmark.png")
    plt.show()

def benchmark_rsa():
    rsa_sizes = [512, 1024, 2048]  # Practical RSA key sizes in bits
    results = []
    sample_text = "RSA timing benchmark sample text."

    for size in rsa_sizes:
        priv, pub = generate_rsa_key(size)
        start = time.time()
        ct = encrypt_rsa(sample_text, pub)
        pt = decrypt_rsa(ct, priv)
        end = time.time()
        results.append(end - start)

    plt.figure()
    plt.plot(rsa_sizes, results, marker='o', color='r', label="RSA")
    plt.title("RSA Encryption/Decryption Execution Time")
    plt.xlabel("Key Size (bits)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig("RSA_benchmark.png")
    plt.show()

if __name__ == "__main__":
    print("Running AES benchmarks...")
    benchmark_aes()
    print("Running RSA benchmarks...")
    benchmark_rsa()
