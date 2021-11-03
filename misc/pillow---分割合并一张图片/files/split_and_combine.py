# coding:utf8

from PIL import Image

im = Image.open('raw.jpg')
want_width, want_height = 120, 120

# 分割
for y in range(3):
    for x in range(3):
        # left, upper, right, lower
        box = (want_width*x, want_height*y, want_width*(x+1), want_height*(y+1))
        sub_im = im.crop(box)
        sub_im_name = '{}.jpg'.format(y*3+x)
        sub_im.save(sub_im_name)
im.close()

# 合并
im = Image.new('RGB', (360, 360))
for y in range(3):
    for x in range(3):
        sub_im_name = '{}.jpg'.format(y*3+x)
        sub_im = Image.open(sub_im_name)
        im.paste(sub_im, (want_width*x, want_height*y))
        sub_im.close()

im.save('result.jpg')
