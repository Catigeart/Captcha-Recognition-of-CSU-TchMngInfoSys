from PIL import Image
from numpy import *

for i in range(10000):
    img = array(Image.open('graphs/image' + str(i) + '.jpg').convert('L').point(lambda x: 255 if x > 112 else 0))
    Image.fromarray(img).save('graphs/image' + str(i) + '_clean.jpg')
    img = Image.open('graphs/image' + str(i) + '_clean.jpg')
    for j in range(4):
        img_crop = img.crop((3 + j * 10, 4, 12 + j * 10, 16))
        img_crop.save('graphs/image' + str(i) + '_clean' + str(j) + ".jpg")

