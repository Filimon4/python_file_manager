from typing import List
import json

class CipherAlgo:
    defaultKeys = []
    with open('./keys.json', "r") as f:
        data = json.load(f)
        for i in data:
            defaultKeys.append(data[i])

    print(defaultKeys)
    def __init__(self):
        pass

    def feistel_round(self, left: int, right: int, key: int) -> tuple:
        new_right = left ^ key
        return right, new_right

    def feistel_cipher(self, plaintext: bytes, keys: List[int]) -> bytes:
        if not keys:
            return
        print(plaintext)
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
        if not keys:
            keys = self.defaultKeys
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