import random

class EncryptionAlgorithms:
    def __init__(self, text):
        self.text = text
        self.caesar_shift = random.randint(1, 25)
        self.transposition_key = random.randint(2, 10)

    def caesar_encrypt(self):
        encrypted_text = ""
        for char in self.text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - shift_base + self.caesar_shift) % 26 + shift_base)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text
    
    def transposition_encrypt(self):
        encrypted_text = [''] * self.transposition_key
        for i in range(len(self.text)):
            encrypted_text[i % self.transposition_key] += self.text[i]
        return ''.join(encrypted_text)