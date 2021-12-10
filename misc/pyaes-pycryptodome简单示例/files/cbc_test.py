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

obj = AES.new(key, AES.MODE_CBC, iv)
ciphertext = obj.encrypt(message_padded)
print('ciphertext: {}'.format(ciphertext))

obj2 = AES.new(key, AES.MODE_CBC, iv)
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

obj = pyaes.AESModeOfOperationCBC(key, iv)
ciphertext = obj.encrypt(message_padded)
print('ciphertext: {}'.format(ciphertext))

obj2 = pyaes.AESModeOfOperationCBC(key, iv)
plaintext = obj2.decrypt(ciphertext)
plaintext = strip_PKCS7_padding(plaintext)
print('plaintext: {}'.format(plaintext))
print()

'''
pycryptodome
b'Hello World\x05\x05\x05\x05\x05'
ciphertext: b'\xf8\xca\xeb\x13r\xb2-\xea"=\xed\x07_NL\xd0'
plaintext: b'Hello World'

pyaes
b'Hello World\x05\x05\x05\x05\x05'
ciphertext: b'\xf8\xca\xeb\x13r\xb2-\xea"=\xed\x07_NL\xd0'
plaintext: b'Hello World'
'''