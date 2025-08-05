import hashlib
import base58
from ecdsa import SigningKey, SECP256k1

# Target address to match
TARGET_ADDRESS = "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU"

# Define start and stop keys (as integers)
START_KEY = int("0000000000000000000000000000000000000000000000400000000000000000", 16)
STOP_KEY  = int("00000000000000000000000000000000000000000000007fffffffffffffffff", 16)

def private_key_to_address(private_key_int):
    # Convert to 32-byte hex
    private_key_bytes = private_key_int.to_bytes(32, byteorder='big')

    # Generate public key
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    vk = sk.get_verifying_key()
    pubkey_bytes = b'\x04' + vk.to_string()

    # Hash160
    sha256 = hashlib.sha256(pubkey_bytes).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    hashed_pubkey = b'\x00' + ripemd160

    # Double SHA256 for checksum
    checksum = hashlib.sha256(hashlib.sha256(hashed_pubkey).digest()).digest()[:4]
    address_bytes = hashed_pubkey + checksum

    return base58.b58encode(address_bytes).decode()

# Main brute-force loop
for i in range(START_KEY, STOP_KEY):
    addr = private_key_to_address(i)
    if addr == TARGET_ADDRESS:
        print(f"\n🎯 MATCH FOUND!\nPrivate Key (hex): {hex(i)}\nAddress: {addr}")
        break
    if i % 100000 == 0:
        print(f"Checked: {hex(i)} - {addr}")
