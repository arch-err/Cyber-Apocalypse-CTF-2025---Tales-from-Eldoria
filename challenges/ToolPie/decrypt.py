#!/usr/bin/env python
from Crypto.Cipher import AES
import binascii

# --- CONFIGURATION ---
KEY = "5UUfizsRsP7oOCAq"  # Replace with your full 16-byte key (e.g., "5UUf9pR2XmS8vB3Q")
IV = b'\x00' * 16  # Null IV (from earlier analysis)
ENCRYPTED_FILE = "./tcp_export"  # From pcapng
OUTPUT_FILE = "./tcp_export.dec"

def decrypt_file():
    try:
        # 1. Read encrypted file (handle large files)
        file_size = os.path.getsize(INPUT_FILE)
        print(f"File size: {file_size} bytes")

        with open(INPUT_FILE, "rb") as f:
            encrypted_data = f.read()

        # 2. Pad data if needed (manual PKCS#7)
        if len(encrypted_data) % 16 != 0:
            pad_len = 16 - (len(encrypted_data) % 16)
            encrypted_data += bytes([pad_len] * pad_len)
            print(f"Added {pad_len} bytes padding")

        # 3. Initialize cipher
        cipher = AES.new(KEY.encode(), AES.MODE_CBC, iv=IV)

        # 4. Decrypt in chunks (memory efficiency)
        chunk_size = 1024 * 1024  # 1MB chunks
        with open(OUTPUT_FILE, "wb") as f:
            for i in range(0, len(encrypted_data), chunk_size):
                chunk = encrypted_data[i:i+chunk_size]
                # Ensure chunk
    except:
        print("ERROR")

decrypt_file()
