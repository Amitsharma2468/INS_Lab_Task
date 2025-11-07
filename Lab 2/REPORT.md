# INS Lab 2 — Classical Cipher Cracking Report (English)

## 1. Objective

This lab demonstrates practical attacks against two classic cryptosystems: the **Caesar cipher** and **monoalphabetic substitution ciphers**. The goal is to implement scripts to recover plaintext from ciphertexts, analyze weaknesses, and document the complete thought process.

---

## 2. Environment & Tools

- Language: **Python 3.8+**
- Editor: **Visual Studio Code (VS Code)**
- Platform: Windows (commands shown for PowerShell / Command Prompt)

---

## 3. Project Structure

```
Lab 2/
 ├── src/
 │    ├── caesar_cracker.py
 │    ├── substitution_solver.py
 │    └── utils.py
 ├── data/
 │    ├── cipher_caesar.txt
 │    ├── cipher_sub_1.txt
 │    └── cipher_sub_2.txt
 ├── wordlists/
 │    └── common_words.txt
 ├── outputs/
 │    ├── caesar_plain.txt
 │    ├── sub1_attempt.txt
 │    └── sub2_attempt.txt
 ├── REPORT.md (this file)
 └── README.md
```

---

## 4. How to run (Commands)

Open a terminal and change to the project folder. Example (replace path if needed):

```powershell
cd "E:\INS_Lab_Task\Lab 2"
```

Run the Caesar cracker:

```powershell
python "src/caesar_cracker.py" "data/cipher_caesar.txt" "outputs/caesar_plain.txt"
```

Run the substitution solver for Cipher 1:

```powershell
python "src/substitution_solver.py" "data/cipher_sub_1.txt" "outputs/sub1_attempt.txt"
```

Run the substitution solver for Cipher 2:

```powershell
python "src/substitution_solver.py" "data/cipher_sub_2.txt" "outputs/sub2_attempt.txt"
```

View outputs in terminal (Windows):

```powershell
type "outputs\caesar_plain.txt"
type "outputs\sub1_attempt.txt"
type "outputs\sub2_attempt.txt"
```

---
