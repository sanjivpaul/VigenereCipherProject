# gui/app.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import tkinter as tk
from tkinter import ttk
from vigenere.cipher import encrypt, decrypt

def run_gui():
    def process_text():
        text = input_text.get("1.0", tk.END).strip()
        keyword = keyword_entry.get().strip()
        if not keyword.isalpha():
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "Keyword must only contain letters.")
            return

        if mode.get() == "Encrypt":
            result = encrypt(text, keyword)
        else:
            result = decrypt(text, keyword)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    root = tk.Tk()
    root.title("Vigenère Cipher")

    ttk.Label(root, text="Enter Text:").grid(row=0, column=0, sticky="w")
    input_text = tk.Text(root, height=4, width=50)
    input_text.grid(row=1, column=0, columnspan=2, padx=10)

    ttk.Label(root, text="Keyword:").grid(row=2, column=0, sticky="w")
    keyword_entry = ttk.Entry(root)
    keyword_entry.grid(row=3, column=0, padx=10, pady=5)

    mode = tk.StringVar(value="Encrypt")
    ttk.Radiobutton(root, text="Encrypt", variable=mode, value="Encrypt").grid(row=3, column=1, sticky="w")
    ttk.Radiobutton(root, text="Decrypt", variable=mode, value="Decrypt").grid(row=4, column=1, sticky="w")

    ttk.Button(root, text="Process", command=process_text).grid(row=5, column=0, columnspan=2, pady=10)

    ttk.Label(root, text="Result:").grid(row=6, column=0, sticky="w")
    output_text = tk.Text(root, height=4, width=50)
    output_text.grid(row=7, column=0, columnspan=2, padx=10)

    root.mainloop()

# Add this to run the GUI
if __name__ == "__main__":
    run_gui()