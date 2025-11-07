#!/usr/bin/env python3
# src/substitution_solver.py

import sys
import random
import math
from collections import Counter
from utils import clean_text, apply_mapping, letter_freq

ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def load_common_words(fn="wordlists/common_words.txt"):
    with open(fn, 'r', encoding='utf-8') as f:
        return set([line.strip().lower() for line in f if line.strip()])

COMMON_WORDS = load_common_words()

def freq_init_mapping(cipher):
    # Map most frequent cipher letters to most frequent english letters
    most_common_english = "etaoinshrdlcumwfgypbvkjxqz"
    freqs = letter_freq(cipher)
    sorted_cipher = [p[0] for p in freqs.most_common()]
    mapping = {}
    for i, c in enumerate(sorted_cipher):
        if i < len(most_common_english):
            mapping[c] = most_common_english[i]
    # fill remaining with random assignment
    remaining_plain = [ch for ch in ALPHA if ch not in mapping.values()]
    remaining_cipher = [ch for ch in ALPHA if ch not in mapping.keys()]
    random.shuffle(remaining_plain)
    for c, p in zip(remaining_cipher, remaining_plain):
        mapping[c] = p
    return mapping

def decode_with_map(cipher, mapping):
    return apply_mapping(cipher, mapping)

def score_plaintext(text):
    s = text.lower()
    # score by counting full word matches and penalize '?' occurrences
    score = 0.0
    words = [w.strip(".,;:!?-'\"()[]") for w in s.split()]
    for w in words:
        if w in COMMON_WORDS:
            score += 2.0
        # partial: if contained common short word
        for cw in COMMON_WORDS:
            if len(cw) > 3 and cw in w:
                score += 0.2
    score -= s.count('?') * 0.1
    # prefer moderate space density
    score += max(0, s.count(' ') / (len(s) + 1))
    return score

def random_swap(mapping):
    # swap images of two plaintext letters by swapping two cipher->plain assignments
    m = mapping.copy()
    a, b = random.sample(ALPHA, 2)
    inv = {v:k for k,v in m.items()}
    ca = inv.get(a)
    cb = inv.get(b)
    if ca and cb:
        m[ca], m[cb] = m[cb], m[ca]
    else:
        x, y = random.sample(list(m.keys()), 2)
        m[x], m[y] = m[y], m[x]
    return m

def hill_climb(cipher, iterations=20000, restarts=6):
    best_global = (float('-inf'), None, None)
    for r in range(restarts):
        mapping = freq_init_mapping(cipher)
        current_plain = decode_with_map(cipher, mapping)
        current_score = score_plaintext(current_plain)
        best_local = (current_score, mapping.copy(), current_plain)

        for i in range(iterations):
            cand_map = random_swap(mapping)
            cand_plain = decode_with_map(cipher, cand_map)
            cand_score = score_plaintext(cand_plain)
            # accept if better, otherwise sometimes accept (simulated annealing idea)
            if cand_score > current_score or random.random() < 0.001:
                mapping = cand_map
                current_score = cand_score
                current_plain = cand_plain
                if cand_score > best_local[0]:
                    best_local = (cand_score, mapping.copy(), current_plain)

        print(f"Restart {r+1}/{restarts} best_local_score={best_local[0]:.2f}")
        if best_local[0] > best_global[0]:
            best_global = best_local

    return best_global

def main():
    if len(sys.argv) < 3:
        print("Usage: python src/substitution_solver.py input_file output_file")
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        cipher = f.read().strip()

    best_score, best_map, best_plain = hill_climb(cipher, iterations=15000, restarts=6)
    print("\nBEST SCORE:", best_score)
    print("\n---- BEST PLAINTEXT SAMPLE ----\n")
    print(best_plain[:2000])
    with open(sys.argv[2], 'w', encoding='utf-8') as out:
        out.write(best_plain)
    print(f"\nWritten best attempt to {sys.argv[2]}")

if __name__ == "__main__":
    main()

