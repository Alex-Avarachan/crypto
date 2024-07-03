#!/usr/bin/env python
# https://en.bitcoin.it/wiki/Protocol_documentation#Addresses

import hashlib
import base58

# ECDSA bitcoin Public Key
pubkey = '7c154ed1dc59609e3d26abb2df2ea3d587cd8c41'
# See 'compressed form' at https://en.bitcoin.it/wiki/Protocol_documentation#Signatures
compress_pubkey = False


def hash160(hex_str):
    sha = hashlib.sha256()
    rip = hashlib.new('ripemd160')
    sha.update(hex_str)
    rip.update( sha.digest() )
    print ( "key_hash = \t" + rip.hexdigest() )
    return rip.hexdigest()  # .hexdigest() is hex ASCII


if (compress_pubkey):
    if (ord(bytearray.fromhex(pubkey[-2:])) % 2 == 0):
        pubkey_compressed = '02'
    else:
        pubkey_compressed = '03'
    pubkey_compressed += pubkey[2:66]
    hex_str = bytearray.fromhex(pubkey_compressed)
else:
    hex_str = bytearray.fromhex(pubkey)

# Obtain key:

key_hash = '00' + "7a28a03d34bf51169f38875640a9b07fa8a06876"

# Obtain signature:

sha = hashlib.sha256()
sha.update( bytearray.fromhex(key_hash) )
checksum = sha.digest()
sha = hashlib.sha256()
sha.update(checksum)
checksum = sha.hexdigest()[0:8]

print ( "checksum = \t" + sha.hexdigest() )
print ( "key_hash + checksum = \t" + key_hash + ' ' + checksum )
print ( "bitcoin address = \t" + (base58.b58encode( bytes(bytearray.fromhex(key_hash + checksum)) )).decode('utf-8') )
print ( "bitcoin address = \t" + (base58.b58encode( bytes(bytearray.fromhex(pubkey)) )).decode('utf-8') )
