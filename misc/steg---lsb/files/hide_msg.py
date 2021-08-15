# coding:utf8
# python3

from PIL import Image

msg = 'flag{hello_world}'
bit_list = []
for i in msg:
    tmp = ord(i)
    bit_tmp = 0b10000000
    for j in range(8):
        if tmp & bit_tmp:
            bit_list.append(1)
        else:
            bit_list.append(0)
        bit_tmp = bit_tmp >> 1
bit_list_len = len(bit_list)

im = Image.open('steg.bmp')
pic = im.load()
w, h = im.size

bit_postion = 0
for i in range(h):
    for j in range(w):
        r, g, b = im.getpixel((j, i))
        new_pix_list = [r, g, b]
        for k in range(3):
            if bit_postion < bit_list_len:
                if bit_list[bit_postion] == 1:
                    new_pix_list[k] = new_pix_list[k] | 0b00000001
                else:
                    new_pix_list[k] = new_pix_list[k] & 0b11111110
                bit_postion+=1
            else:
                break
        pic[j, i] = (new_pix_list[0], new_pix_list[1], new_pix_list[2])

        if bit_postion >= bit_list_len:
            im.save('steg_lsb.bmp')
            im.close()
            exit(0)