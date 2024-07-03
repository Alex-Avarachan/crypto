import hashlib
import base58

def generate_bitcoin_address(public_key):
  """Generates a Bitcoin address from a public key.

  Args:
    public_key: The public key in hexadecimal format.

  Returns:
    The Bitcoin address in base58 format.
  """

  # Convert the public key to a byte array.
  public_key_bytes = bytearray.fromhex(public_key)

  # Hash the public key.
  hash_1 = hashlib.sha256(public_key_bytes).digest()
  h = hashlib.new("ripemd160")
  h.update(hash_1)
  hash_2 = h.hexdigest()
  hash_2 = bytearray.fromhex(hash_2)
  print(hash_2)

  # Add the version byte and checksum.
  address_bytes = bytearray([0x00]) + hash_2 + bytearray(base58.encode(hash_2))[:4]

  # Encode the address in base58.
  address = base58.encode(address_bytes).decode()

  return address


# Example usage:

public_key = "046788ae4aaf49a720372873773b1a92637b643b233f07375f212272273347755384a52b27737463383833873745383838737453838387"
address = generate_bitcoin_address(public_key)

print(address)