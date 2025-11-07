# Lab 2 — Attacking Classic Crypto Systems

This repository contains code, data and a report template for **Lab 2: Attacking Classic Crypto Systems**.

## What is included

- `src/caesar_cracker.py` — brute-force Caesar cipher cracker.
- `src/substitution_solver.py` — substitution cipher solver using frequency init + hill-climbing.
- `data/` — ciphertext files.
- `wordlists/common_words.txt` — common English words for scoring.
- `REPORT.md` — lab report template with methodology and checkpoints.
- `outputs/` — where output plaintexts will be saved.

## Requirements

- Python 3.8+
- No external pip packages required (pure Python).

## How to run (VS Code)

1. Open the repository folder in VS Code.
2. (Optional) Create & activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # mac/linux
   .venv\Scripts\activate      # windows
   ```
