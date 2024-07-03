import hashlib
import binascii


if __name__ == '__main__':
	hexadecimal = hex(1281295)
	#hexadecimal = "0x0f8d13"
	print("hex : " + hexadecimal)
	hex_string = hexadecimal[2:]
	hex_string = "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4b03a0d909fabe6d6da46f55f209ae99b83d01196263c7ef18a223cd2d79260b4efb155f962619960b01000000000000000165010057d9f7c82c00000000000075ae4f83052f736c7573682f000000000435bda32b000000001976a9147c154ed1dc59609e3d26abb2df2ea3d587cd8c4188ac00000000000000002c6a4c2952534b424c4f434b3a40777a5f1de0727bb1bced1b8bc51927b116a43aa8f7bd279550862e00286ba60000000000000000296a4c266a24b9e11b6db57eacad1470f16a4353a4a351aab537f3d2a54b59c4d1f3e384bee1e4a783fc0000000000000000266a24aa21a9edc44cc85fe716fa85c86b15db56c652a06435989d25f7d0c8e267bd593046af0100000000"
	print("hex string : " + hex_string)
	little_endian_hex = bytearray.fromhex(hex_string)[::-1]
	little_endian_hex_string = binascii.hexlify(little_endian_hex).decode()
	print("hex string decoded : " + little_endian_hex_string)


	blockheader = hex_string
	print("coinbase : " + blockheader)
	hash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(blockheader)).digest()).digest()
	print("hash : " + str(hash))
	hash = binascii.hexlify(hash).decode()
	print("blockheader hash : " + hash)

	txid = binascii.hexlify(binascii.unhexlify(hash)[::-1])
	txid = str(txid,"ascii")
	print("txnid : " + txid)

	print(hashlib.algorithms_available)

	key = "7c154ed1dc59609e3d26abb2df2ea3d587cd8c41"
	h = hashlib.new('ripemd160')
	value = h.update(hashlib.sha256(binascii.unhexlify(key)).digest()).hexdigest()

	print(value)

	print("value : " + binascii.hexlify(value).decode())




