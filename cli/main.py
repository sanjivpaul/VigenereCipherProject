# cli/main.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vigenere.cipher import encrypt, decrypt

def main():
    print("=== Vigenère Cipher CLI ===")
    choice = input("Encrypt or Decrypt? (e/d): ").strip().lower()

    if choice not in ("e", "d"):
        print("Invalid choice.")
        return

    keyword = input("Enter keyword: ").strip()
    if not keyword.isalpha():
        print("Keyword must only contain letters.")
        return

    text = input("Enter text: ")

    if choice == "e":
        result = encrypt(text, keyword)
        print("Encrypted text:", result)
    else:
        result = decrypt(text, keyword)
        print("Decrypted text:", result)

if __name__ == "__main__":
    main()
