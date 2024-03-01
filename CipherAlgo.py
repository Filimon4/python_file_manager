import base64
from typing import List

class CipherAlgo:
    def __init__(self):
        self.defaultKeys = [0xA1B2C3D4, 0xE5F67890, 0x1A2B3C4D, 0x5E6F7890]
        self.input = ''
        self.output = ''

    def feistel_round(self, left: int, right: int, key: int) -> tuple:
        new_right = left ^ key
        return right, new_right

    def feistel_cipher(self, plaintext: bytes, keys: List[int]) -> bytes:
        padding_length = 8 - (len(plaintext) % 8)
        plaintext += bytes([padding_length] * padding_length)

        blocks = [plaintext[i:i+8] for i in range(0, len(plaintext), 8)]
        ciphertext = b''

        for block in blocks:
            block_int = int.from_bytes(block, byteorder='big')
            left = block_int >> 32
            right = block_int & 0xFFFFFFFF

            for key in keys:
                left, right = self.feistel_round(left, right, key)

            left, right = right, left

            cipher_block = (left << 32 | right).to_bytes(8, byteorder='big')
            ciphertext += cipher_block

        return ciphertext

    def feistel_decipher(self, ciphertext: bytes, keys: List[int]) -> bytes:
        blocks = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]
        plaintext = b''

        for block in blocks:
            block_int = int.from_bytes(block, byteorder='big')
            left = block_int >> 32
            right = block_int & 0xFFFFFFFF

            for key in reversed(keys):
                left, right = self.feistel_round(left, right, key)

            left, right = right, left

            plain_block = (left << 32 | right).to_bytes(8, byteorder='big')
            plaintext += plain_block

        padding_length = plaintext[-1]
        plaintext = plaintext[:-padding_length]

        return plaintext

    # def cipher(self):
    #     pass
    #     # get input file
    #     # cipher file
    #     # outfile in .b64 with original name

    # def decipher(self):
    #     pass
    #     # get input file .b64 format
    #     # decipher file
    #     # outifle with original name and format

    # def main(self):

    #     command = int(input("1 or 2: "))
    #     if command == 1:
    #         with open('input', 'rb') as file:
    #             plain_text = file.read()
    #         plain_text = base64.b64encode(plain_text)
    #         ciphertext = self.feistel_cipher(plain_text, keys)
    #         with open('output', 'wb') as file:
    #             file.write(ciphertext)
    #     elif command == 2:
    #         with open('input', 'rb') as file:
    #             plain_text = file.read()
    #         ciphertext = self.feistel_decipher(plain_text, keys)
    #         with open('output', 'wb') as file:
    #             file.write(base64.b64decode(ciphertext))

class Encrypt(CipherAlgo):

    def __init__(self, app):
        super().__init__()
        self.app = app

        self.actionCipher = self.app.ui.actionCipher
        self.actionCipher.triggered.connect(self.actionClicked)

    def actionClicked(self):
        print('cipherStart')


class Decrypt(CipherAlgo):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.actionDecipher = self.app.ui.actionDecipher
        self.actionDecipher.triggered.connect(self.actionClicked)

    def actionClicked(self):
        print('decipherStart')

