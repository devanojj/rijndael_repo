import ctypes

# Load your compiled AES library
rijndael = ctypes.CDLL('./rijndael.dll')

# Define function signatures
rijndael.aes_encrypt_block.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
rijndael.aes_encrypt_block.restype = ctypes.POINTER(ctypes.c_ubyte)

rijndael.aes_decrypt_block.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
rijndael.aes_decrypt_block.restype = ctypes.POINTER(ctypes.c_ubyte)

# 3 Test cases
test_cases = [
    (
        bytes.fromhex("00112233445566778899aabbccddeeff"),
        bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    ),
    (
        bytes.fromhex("6bc1bee22e409f96e93d7e117393172a"),
        bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
    ),
    (
        bytes.fromhex("ae2d8a571e03ac9c9eb76fac45af8e51"),
        bytes.fromhex("f69f2445df4f9b17ad2b417be66c3710")
    )
]

for i, (plaintext_bytes, key_bytes) in enumerate(test_cases):
    print(f"\nTest #{i+1}")

    # Convert Python bytes to C types
    plaintext = (ctypes.c_ubyte * 16)(*plaintext_bytes)
    key = (ctypes.c_ubyte * 16)(*key_bytes)

    # Encrypt
    cipher_ptr = rijndael.aes_encrypt_block(plaintext, key)
    ciphertext = bytes(cipher_ptr[:16])
    print(f"Encrypted: {ciphertext.hex()}")

    # Decrypt
    plain_ptr = rijndael.aes_decrypt_block(cipher_ptr, key)
    decrypted = bytes(plain_ptr[:16])
    print(f"Decrypted: {decrypted.hex()}")

    # Verify
    if decrypted == plaintext_bytes:
        print("Correct")
    else:
        print("Failed")