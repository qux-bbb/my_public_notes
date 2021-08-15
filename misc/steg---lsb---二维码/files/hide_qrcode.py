# coding:utf8
# python3

'''
把二维码图片写到新图片的红色图层最低位
'''

from PIL import Image

im_qrcode = Image.open('qrcode.png')
pic_qrcode = im_qrcode.load()
w_qrcode, h_qrcode = im_qrcode.size

im_raw = Image.open('raw.png')
pic_raw = im_raw.load()
w_raw, h_raw = im_raw.size


for i in range(h_qrcode):
    for j in range(w_qrcode):
        r_qrcode, g_qrcode, b_qrcode = pic_qrcode[j, i]
        r_raw, g_raw, b_raw = pic_raw[j, i]
        if r_qrcode == 255:
            r_raw = r_raw | 0b00000001
        else:
            r_raw = r_raw & 0b11111110
        pic_raw[j, i] = (r_raw, g_raw, b_raw)
im_raw.save('dst.png')

im_qrcode.close()
im_raw.close()
