import base64
from typing import List

class CipherAlgo:
    defaultKeys = [0xA1B2C3D4, 0xE5F67890, 0x1A2B3C4D, 0x5E6F7890]
    def __init__(self):
        self.input = ''
        self.output = ''

    def feistel_round(self, left: int, right: int, key: int) -> tuple:
        new_right = left ^ key
        return right, new_right

    def feistel_cipher(self, plaintext: bytes, keys: List[int] = defaultKeys) -> bytes:
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

    def feistel_decipher(self, ciphertext: bytes, keys: List[int] = defaultKeys) -> bytes:
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

class Encrypt(CipherAlgo):

    def __init__(self, app):
        super().__init__()
        self.app = app

        self.actionCipher = self.app.ui.actionCipher
        self.actionCipher.triggered.connect(self.actionClicked)

    def actionClicked(self):
        selectedFile = self.app.FileV.getSingleSelectedFile()
        fileName = self.app.FileS.engine.fileName(selectedFile)
        readBinary = self.app.FileO.readBinaryFile(selectedFile)
        plain_text = base64.b64encode(readBinary)
        ciphertext = str.encode(f"{fileName}") + str.encode("\n") + super().feistel_cipher(plain_text)
        self.app.FileO.newFileBinarySilent(f"{fileName.split('.')[0]}.b64", ciphertext)


class Decrypt(CipherAlgo):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.actionDecipher = self.app.ui.actionDecipher
        self.actionDecipher.triggered.connect(self.actionClicked)

    def actionClicked(self):
        selectedFile = self.app.FileV.getSingleSelectedFile()
        readBinary = self.app.FileO.readBinaryFile(selectedFile)
        fileName, cipher = readBinary.split(b'\n')
        deciphertext = super().feistel_decipher(cipher)
        self.app.FileO.newFileBinarySilent(f"{fileName.decode()}", base64.b64decode(deciphertext))

