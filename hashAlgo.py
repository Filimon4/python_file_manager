import struct

class MD5:
    def __init__(self):
        self.A = 0x67452301
        self.B = 0xEFCDAB89
        self.C = 0x98BADCFE
        self.D = 0x10325476
        self.buffer = b''
        self.count = 0

    def _update(self, data):
        self.buffer += data
        self.count += len(data)

        while len(self.buffer) >= 64:
            block = self.buffer[:64]
            self.buffer = self.buffer[64:]
            self._process_block(block)

    def update(self, data):
        if isinstance(data, str):
            data = data.encode()
        self._update(data)

    def _process_block(self, block):
        a, b, c, d = self.A, self.B, self.C, self.D
        x = [int.from_bytes(block[i:i+4], byteorder='little') for i in range(0, len(block), 4)]

        a = self._round(a, b, c, d, x[0])
        d = self._round(d, a, b, c, x[1])
        b = self._round(b, c, d, a, x[2])
        c = self._round(c, d, a, b, x[3])

        # Update hash state
        self.A = (self.A + a) & 0xFFFFFFFF
        self.B = (self.B + b) & 0xFFFFFFFF
        self.C = (self.C + c) & 0xFFFFFFFF
        self.D = (self.D + d) & 0xFFFFFFFF

    def _round(self, h1, h2, h3, h4, x):
        a = h2 + (h1 + ((h2 & h3) | (~h2 & h4)) + x)
        return a & 0xFFFFFFFF

    def digest(self):
        self._update(b'\x80' + b'\x00' * ((56 - (self.count + 1) % 64) % 64))
        self._update(struct.pack('<Q', self.count * 8))
        return struct.pack('<4I', self.A, self.B, self.C, self.D)

    def hexdigest(self):
        return self.digest().hex()

