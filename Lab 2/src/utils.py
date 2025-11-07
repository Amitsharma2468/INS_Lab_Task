# src/utils.py
import string
from collections import Counter

def clean_text(s):
    """Lowercase, keep letters and spaces, replace others with spaces"""
    return ''.join(c.lower() if c.isalpha() or c.isspace() else ' ' for c in s)

def letter_freq(s):
    """Return Counter of letters in s"""
    s2 = [c for c in s.lower() if c.isalpha()]
    return Counter(s2)

def apply_mapping(text, mapping):
    """Apply mapping: mapping maps cipher_letter->plaintext_letter"""
    out = []
    for c in text:
        if c.isalpha():
            low = c.lower()
            if low in mapping:
                dec = mapping[low]
                out.append(dec.upper() if c.isupper() else dec)
            else:
                out.append('?')
        else:
            out.append(c)
    return ''.join(out)
