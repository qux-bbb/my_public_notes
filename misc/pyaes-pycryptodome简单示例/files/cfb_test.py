# coding:utf8

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import pyaes
from pyaes.util import append_PKCS7_padding, strip_PKCS7_padding

print('pycryptodome')
message = b'Hello World'
key = b'This is a key123'
iv = b'This is an IV456'
message_padded = pad(message, block_size=16)
print(message_padded)

obj = AES.new(key, AES.MODE_CFB, iv, segment_size=16)
ciphertext = obj.encrypt(message_padded)
print('ciphertext: {}'.format(ciphertext))

obj2 = AES.new(key, AES.MODE_CFB, iv, segment_size=16)
plaintext = obj2.decrypt(ciphertext)
plaintext = unpad(plaintext, block_size=16)
print('plaintext: {}'.format(plaintext))
print()


print('pyaes')
message = b'Hello World'
key = b'This is a key123'
iv = b'This is an IV456'
message_padded = append_PKCS7_padding(message)
print(message_padded)

obj = pyaes.AESModeOfOperationCFB(key, iv, segment_size = 16)
ciphertext = obj.encrypt(message_padded)
print('ciphertext: {}'.format(ciphertext))

obj2 = pyaes.AESModeOfOperationCFB(key, iv, segment_size = 16)
plaintext = obj2.decrypt(ciphertext)
plaintext = strip_PKCS7_padding(plaintext)
print('plaintext: {}'.format(plaintext))
print()

'''
pycryptodome
b'Hello World\x05\x05\x05\x05\x05'
ciphertext: b'\xc56\x9cW4\x8a\xceu\xc0\xae*\x87=0\x90#'
plaintext: b'Hello World'

pyaes
b'Hello World\x05\x05\x05\x05\x05'
ciphertext: b'\xc56\xfc\xeb\x9b\xe7\xf3\xcf\x16qV!%\xcf\x832'
plaintext: b'Hello World'
'''