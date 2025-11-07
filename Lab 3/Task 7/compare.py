def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string)*4)

def count_same_bits(hex1, hex2):
    bin1 = hex_to_binary(hex1)
    bin2 = hex_to_binary(hex2)
    same_bits = sum(1 for a, b in zip(bin1, bin2) if a == b)
    total_bits = len(bin1)
    return same_bits, total_bits

hash1 = "fb3f576270378511030d580230454fae14b6cd8caa00a544febdbff82c44dbc2"  # Original Hash Value
hash2 = "f2ee473f251f398759579d74c007d403516c34fc5f8cbc66a6441406e18e9ded"  # Modified Hash Value

same, total = count_same_bits(hash1, hash2)
print(f"Same bits: {same}/{total} ({same/total*100:.2f}%)")