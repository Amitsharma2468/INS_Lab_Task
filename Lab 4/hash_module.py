from Crypto.Hash import SHA256

def hash_sha256(file_path):
    h = SHA256.new()
    with open(file_path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()
