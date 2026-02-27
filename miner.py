# CPU Mining Logic for Bitcoin and Litecoin

import hashlib
import time
import struct

class CPUMiner:
    def __init__(self, target_bits, nonce_start=0):
        self.target = self.calculate_target(target_bits)
        self.nonce = nonce_start

    def calculate_target(self, bits):
        # Convert bits to target
        exponent = bits[0]
        coefficient = int.from_bytes(bits[1:], 'big')
        return coefficient * (2 ** (8 * (exponent - 3)))

    def mine(self, block_header):
        while True:
            header_with_nonce = block_header + struct.pack('I', self.nonce)
            hash_result = hashlib.sha256(hashlib.sha256(header_with_nonce).digest()).digest()
            hash_int = int.from_bytes(hash_result, 'big')

            if hash_int < self.target:
                print(f"Successful mining! Nonce: {self.nonce}, Hash: {hash_result.hex()}")
                return self.nonce, hash_result.hex()

            self.nonce += 1

# Example usage
if __name__ == '__main__':
    target_bits = [0x1b, 0x4c, 0x4a, 0x77, 0x6a, 0x6f, 0x72, 0x29, 0x00]
    miner = CPUMiner(target_bits)
    block_header = b'example_block_header'
    miner.mine(block_header)