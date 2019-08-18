import os
from PIL import Image
import numpy as np
from keras.models import load_model

model = load_model("PredictModel.h5")

character_list = ['1', '2', '3', 'b', 'c', 'm', 'n', 'v', 'x', 'z']
img_path = 'unpredict/'
if not os.path.exists(img_path):
    os.makedirs(img_path)
images_name = os.listdir(img_path)
if not os.path.exists('predicted/'):
    os.makedirs('predicted')
for img_name in images_name:
    img_np = np.array(Image.open(img_path + img_name))
    img_pic = Image.open(img_path + img_name)
    v = img_np.reshape(img_np.shape[0] * img_np.shape[1], 1)
    v = v / 255
    pre = model.predict(v.T)
    max = 0
    p = -1
    for i in range(0, 10):
        if pre[0, i] > max:
            max = pre[0, i]
            p = i
    print('--------------------')
    print(p)
    print(max)
    img_pic.save('predicted/' + character_list[p] + '/' + img_name)



