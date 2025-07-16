# Vigenere Cipher Cryptography

### Folder Structure

```bash
vigenere_cipher_project/
├── vigenere/
│   ├── __init__.py
│   └── cipher.py       # Vigenère cipher logic
├── cli/
│   ├── __init__.py
│   └── main.py         # Command-line interface
├── gui/
│   ├── __init__.py
│   └── app.py          # Tkinter GUI
├── requirements.txt
└── README.md
```

### Output

```bash
(.venv) v1macbookair@V1s-Air-2 vigenere_cipher_project % python -m cli.main

=== Vigenère Cipher CLI ===
Encrypt or Decrypt? (e/d): e
Enter keyword: sun
Enter text: sanjiv
Encrypted text: KUABCI

(.venv) v1macbookair@V1s-Air-2 vigenere_cipher_project % python -m cli.main

=== Vigenère Cipher CLI ===
Encrypt or Decrypt? (e/d): d
Enter keyword: sun
Enter text: KUABCI
Decrypted text: SANJIV

```
