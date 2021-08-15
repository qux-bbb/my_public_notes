# coding:utf8
# python3

import re
from PIL import Image

im = Image.open('steg_lsb.bmp')

w, h = im.size

hide_bits = ''
for i in range(h):
    for j in range(w):
        r, g, b = im.getpixel((j, i))
        for tmp in [r, g, b]:
            if tmp & 1:
                hide_bits += '1'
            else:
                hide_bits += '0'

result = ''
hide_byte_str_list = re.findall(r'.{8}', hide_bits)
for hide_byte_str in hide_byte_str_list:
    tmp = chr(int(hide_byte_str, 2))
    result += tmp
# 直接输出看起来是乱码，显示有问题，写到文件里看就可以了
print(result[:100])
open('result.txt', 'wb').write(result[:100].encode())

im.close()