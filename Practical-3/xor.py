#A XOR B = B XOR A

A_hex_str = "67af3f01"
B_hex_str = "9fa76fbb"
C_hex_str = "f6d4d9ba"
Z_hex_str = "00000000"

A_bytes = bytes.fromhex(A_hex_str)
B_bytes = bytes.fromhex(B_hex_str)
C_bytes = bytes.fromhex(C_hex_str)
Z_bytes = bytes.fromhex(Z_hex_str)

def xor_bytes(bytes_seq_1, bytes_seq_2):
    """Performs an XOR on two bytes sequences"""
    return bytes([a ^ b for a, b in zip(bytes_seq_1, bytes_seq_2)])

t0 = xor_bytes(A_bytes, B_bytes)
t1 = xor_bytes(B_bytes, A_bytes)

print(t0.hex())
print(t1.hex())

t2 = xor_bytes(A_bytes, xor_bytes(B_bytes, C_bytes))
t3 = xor_bytes(xor_bytes(A_bytes, B_bytes), C_bytes)

print(t2.hex())
print(t3.hex())

t4 = xor_bytes(A_bytes, Z_bytes)

print(t4.hex())
print(A_bytes.hex())

t5 = xor_bytes(B_bytes, B_bytes)
print(t5.hex())
print(Z_bytes.hex())