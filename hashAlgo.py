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

        # Round 1
        a = self._round1(a, b, c, d, x[0], 7, 0xd76aa478)
        d = self._round1(d, a, b, c, x[1], 12, 0xe8c7b756)

        # Round 2
        b = self._round2(b, c, d, a, x[2], 17, 0x242070db)
        c = self._round2(c, d, a, b, x[3], 22, 0xc1bdceee)

        # Update hash state
        self.A = (self.A + a) & 0xFFFFFFFF
        self.B = (self.B + b) & 0xFFFFFFFF
        self.C = (self.C + c) & 0xFFFFFFFF
        self.D = (self.D + d) & 0xFFFFFFFF

    def _round1(self, a, b, c, d, x, s, t):
        a = b + ((a + ((b & c) | (~b & d)) + x + t) << s)
        return a & 0xFFFFFFFF

    def _round2(self, a, b, c, d, x, s, t):
        a = b + ((a + ((b & d) | (c & ~d)) + x + t) << s)
        return a & 0xFFFFFFFF

    def digest(self):
        # Append padding to the data
        self._update(b'\x80' + b'\x00' * ((56 - (self.count + 1) % 64) % 64))
        self._update(struct.pack('<Q', self.count * 8))

        # Return the digest
        return struct.pack('<4I', self.A, self.B, self.C, self.D)

    def hexdigest(self):
        # Return the digest as a hex string
        return self.digest().hex()

