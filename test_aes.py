import ctypes

# Load the DLL
rijndael = ctypes.CDLL('./rijndael.dll')


rijndael.aes_encrypt_block.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
rijndael.aes_encrypt_block.restype = ctypes.POINTER(ctypes.c_ubyte)

rijndael.aes_decrypt_block.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
rijndael.aes_decrypt_block.restype = ctypes.POINTER(ctypes.c_ubyte)


plaintext = (ctypes.c_ubyte * 16)(*range(1, 17))  # [1, 2, ..., 16]
key = (ctypes.c_ubyte * 16)(*range(16))           # [0, 1, ..., 15]

# Encrypt
cipher_ptr = rijndael.aes_encrypt_block(plaintext, key)
cipher = bytes(cipher_ptr[:16])
print("Encrypted:", cipher)

# Decrypt
plain_ptr = rijndael.aes_decrypt_block(cipher_ptr, key)
decrypted = bytes(plain_ptr[:16])
print("Decrypted:", decrypted)