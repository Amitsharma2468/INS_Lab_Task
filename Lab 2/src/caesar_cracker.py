#!/usr/bin/env python3
# src/caesar_cracker.py

import sys
from utils import clean_text

def caesar_decrypt(text, shift):
    res = []
    for c in text:
        if c.isalpha():
            base = ord('a')
            res.append(chr((ord(c) - base - shift) % 26 + base))
        else:
            res.append(c)
    return ''.join(res)

def score_guess(plain):
    commons = [" the ", " and ", " to ", " of ", " a ", " in ", " is ", " that ", " there "]
    s = plain.lower()
    return sum(s.count(w) for w in commons)

def main():
    if len(sys.argv) < 3:
        print("Usage: python src/caesar_cracker.py input_file output_file")
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        cipher = f.read().strip()

    best = []
    for shift in range(26):
        plain = caesar_decrypt(cipher, shift)
        sc = score_guess(' ' + plain + ' ')
        best.append((sc, shift, plain))

    best.sort(reverse=True, key=lambda x: x[0])
    print("Top candidates (score, shift):")
    for sc, shift, plain in best[:8]:
        print(f"shift={shift:2d}  score={sc:2d}  -> {plain}")

    top = best[0][2]
    with open(sys.argv[2], 'w', encoding='utf-8') as out:
        out.write(top)
    print(f"\nBest candidate written to {sys.argv[2]}")

if __name__ == "__main__":
    main()
