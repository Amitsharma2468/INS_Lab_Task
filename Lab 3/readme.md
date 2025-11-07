# Task 1

## CBC encryption:

```bash
openssl enc -aes-128-cbc -e -in plain.txt -out out-cbc.bin -K
00112233445566778899aabbccddeeff -iv 0102030405060708
```

## ECB encryption:

```bash
openssl enc -aes-128-ecb -e -in plain.txt -out out-ecb.bin -K
00112233445566778899aabbccddeeff
```

## CFB encryption:

```bash
openssl enc -aes-128-cfb -e -in plain.txt -out out-cfb.bin -K
00112233445566778899aabbccddeeff -iv 0102030405060708
```

# Task 2

## Image ECB encryption:

```bash
openssl enc -aes-128-ecb -e -in pic_original.bmp -out pic_ecb.bin -K 00112233445566778899aabbccddeeff
```

## Image CBC encryption:

```bash
openssl enc -aes-128-cbc -e -in pic_original.bmp -out pic_cbc.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708
```

# Task 3

## ECB

### Encryption:

```bash
openssl enc -aes-128-ecb -e -in long_text.txt -out encrypted_ecb.bin -K 00112233445566778889aabbccddeeff
```

### Decryption:

```bash
openssl enc -aes-128-ecb -d -in corrupted_ecb.bin -out corrupted_ecb.txt -K 00112233445566778889aabbccddeeff
```

## CBC

### Encryption:

```bash
openssl enc -aes-128-cbc -e -in long_text.txt -out encrypted_cbc.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

### Decryption:

```bash
openssl enc -aes-128-cbc -d -in corrupted_cbc.bin -out corrupted_cbc.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

## CFB

### Encryption:

```bash
openssl enc -aes-128-cfb -e -in long_text.txt -out encrypted_cfb.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

### Decryption:

```bash
openssl enc -aes-128-cfb -d -in corrupted_cfb.bin -out corrupted_cfb.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

## OFB

### Encryption:

```bash
openssl enc -aes-128-ofb -e -in long_text.txt -out encrypted_ofb.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

### Decryption:

```bash
openssl enc -aes-128-ofb -d -in corrupted_ofb.bin -out corrupted_ofb.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

# Task 4

## ECB

```bash
openssl enc -aes-128-ecb -e -in short.txt -out short_ecb.bin -K 00112233445566778889aabbccddeeff
```

## CBC

```bash
openssl enc -aes-128-cbc -e -in short.txt -out short_cbc.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

## CFB

```bash
openssl enc -aes-128-cfb -e -in short.txt -out short_cfb.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

## OFB

```bash
openssl enc -aes-128-ofb -e -in short.txt -out short_ofb.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

# Task 5

## Hasing

### MD5

Command:

```bash
openssl dgst -md5 hash_sample.txt
```

Output: 8c840e2a4cf16f39c00f05ae0bebb02a

### SHA1

Command:

```bash
openssl dgst -sha1 hash_sample.txt
```

Output: 91eb45b52babf4500cc578e6492e1dad0342d34f

### SHA 256

Command:

```bash
openssl dgst -sha256 hash_sample.txt
```

Output: f2a3af0327329e7d3b74501f36cedf018f7b3126c28647d9eae221142503bc4c

### SHA 512

Command:

```bash
openssl dgst -sha512 hash_sample.txt
```

Output: 8544fe3dfdaa96c8d4d645c5d22004b52fc787395c441e54eecf7d51d73c534b25dfbfe15ca1bc583260a06d13a1a07f52a4d9252c129ed45ac295f84b5fef1a

# Task 6

### Short key

```
openssl dgst -md5 -hmac "mykey" hmac_test.txt
```

Output: 3729da33b418a9d4125c5e27c229b945

```
openssl dgst -sha1 -hmac "mykey" hmac_test.txt
```

Output: be3a0e2f20613fa47ccfe36c518823532a4e556b

```
openssl dgst -sha256 -hmac "mykey" hmac_test.txt
```

Output: 5394e084fbe91c6d398873a68293f1a393d86670285d8c9beed212148b1c68eb

### Long key

```
openssl dgst -md5 -hmac "thisisaverylongkeythatismuchlongerthanexpected" hmac_test.txt
```

Output: 6abda667b8eb6da1d66486a877ef25fa

### Very short key

```
openssl dgst -sha256 -hmac "a" hmac_test.txt
```

Output: 58c9a50e26b503c80d39e106cb588b9cf8a8c28b36f1af05267f841857f750ca

Answer: HMAC doesn't require fixed key size. The key is hashed to the appropriate block size internally.

# Task 7

## Hasing Original File

### MD5

```
openssl dgst -md5 hash_original.txt > H1_md5.txt
```

### SHA 256

```
openssl dgst -sha256 hash_original.txt > H1_sha256.txt
```

## Hasing Modified File

### MD5

```
openssl dgst -md5 hash_modified.txt > H2_md5.txt
```

### SHA 256

```
openssl dgst -sha256 hash_modified.txt > H2_sha256.txt
```

## Python script for bit comparison

### Code: [Source](./Task%207/compare.py)

### Result:

- MD5: Same bits: 65/128 (50.78%)
- SHA 256: Same bits: 127/256 (49.61%)
