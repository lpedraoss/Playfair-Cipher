import os

class PlayfairCipher:
    def __init__(self, key):
        self.size = 5
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        self.key = self.prepare_key(key)
        self.matrix = self.create_matrix()

    def prepare_key(self, key):
        key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Elimina duplicados y mantiene el orden
        key = ''.join([c for c in key if c in self.alphabet])  # Elimina caracteres no en el alfabeto
        return key

    def create_matrix(self):
        matrix = []
        used_chars = set(self.key)

        for char in self.key:
            matrix.append(char)

        for char in self.alphabet:
            if char not in used_chars:
                matrix.append(char)

        return [matrix[i:i + self.size] for i in range(0, len(matrix), self.size)]

    def prepare_text(self, text):
        text = ''.join([c for c in text if c in self.alphabet])  # Elimina caracteres no en el alfabeto
        text = text.upper().replace("J", "I")  # Opcional: Reemplaza 'J' por 'I' si usamos el alfabeto inglés tradicional sin 'J'

        prepared_text = []
        i = 0

        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else 'X'

            if a == b:
                prepared_text.append(a + 'X')
                i += 1
            else:
                prepared_text.append(a + b)
                i += 2

        if len(prepared_text[-1]) == 1:
            prepared_text[-1] += 'X'

        return prepared_text

    def find_position(self, char):
        for i, row in enumerate(self.matrix):
            if char in row:
                return i, row.index(char)
        return None

    def encrypt_pair(self, a, b):
        row1, col1 = self.find_position(a)
        row2, col2 = self.find_position(b)

        if row1 == row2:
            return self.matrix[row1][(col1 + 1) % self.size] + self.matrix[row2][(col2 + 1) % self.size]
        elif col1 == col2:
            return self.matrix[(row1 + 1) % self.size][col1] + self.matrix[(row2 + 1) % self.size][col2]
        else:
            return self.matrix[row1][col2] + self.matrix[row2][col1]

    def decrypt_pair(self, a, b):
        row1, col1 = self.find_position(a)
        row2, col2 = self.find_position(b)

        if row1 == row2:
            return self.matrix[row1][(col1 - 1) % self.size] + self.matrix[row2][(col2 - 1) % self.size]
        elif col1 == col2:
            return self.matrix[(row1 - 1) % self.size][col1] + self.matrix[(row2 - 1) % self.size][col2]
        else:
            return self.matrix[row1][col2] + self.matrix[row2][col1]

    def encrypt(self, text):
        prepared_text = self.prepare_text(text)
        encrypted_text = ""

        for pair in prepared_text:
            encrypted_text += self.encrypt_pair(pair[0], pair[1])

        return encrypted_text

    def decrypt(self, text):
        prepared_text = [text[i:i+2] for i in range(0, len(text), 2)]
        decrypted_text = ""

        for pair in prepared_text:
            decrypted_text += self.decrypt_pair(pair[0], pair[1])
        return decrypted_text