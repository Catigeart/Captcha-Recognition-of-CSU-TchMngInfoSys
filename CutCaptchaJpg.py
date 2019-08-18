from PIL import Image
from numpy import *
import os

root = 'graph/'
if not os.path.exists(root):
    os.makedirs(root)

for i in range(10000):
    img = array(Image.open(root + 'image' + str(i) + '.jpg').convert('L').point(lambda x: 255 if x > 112 else 0))
    #灰度化并去除干扰线
    Image.fromarray(img).save(root + 'image' + str(i) + '_clean.jpg')
    img = Image.open(root + 'image' + str(i) + '_clean.jpg')
    for j in range(4):
        img_crop = img.crop((3 + j * 10, 4, 12 + j * 10, 16))
        img_crop.save(root + 'image' + str(i) + '_clean' + str(j) + ".jpg")

