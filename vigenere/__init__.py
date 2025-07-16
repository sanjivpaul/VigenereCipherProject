# vigenere/cipher.py

def format_keyword(keyword, length):
    keyword = keyword.upper()
    return (keyword * (length // len(keyword) + 1))[:length]

def encrypt(text, keyword):
    result = []
    keyword = format_keyword(keyword, len(text))
    for t_char, k_char in zip(text.upper(), keyword):
        if t_char.isalpha():
            shift = ord(k_char) - ord('A')
            base = ord('A')
            result.append(chr((ord(t_char) - base + shift) % 26 + base))
        else:
            result.append(t_char)
    return ''.join(result)

def decrypt(text, keyword):
    result = []
    keyword = format_keyword(keyword, len(text))
    for t_char, k_char in zip(text.upper(), keyword):
        if t_char.isalpha():
            shift = ord(k_char) - ord('A')
            base = ord('A')
            result.append(chr((ord(t_char) - base - shift + 26) % 26 + base))
        else:
            result.append(t_char)
    return ''.join(result)
