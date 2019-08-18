import os
import numpy as np
import requests
from PIL import Image as Im, ImageTk
from numpy import *
from keras.models import load_model
import tkinter as tk
from tkinter import *

def DownImg(url):
    sess = requests.Session()
    img = sess.get(url).content
    with open('img.jpg', 'wb') as f:
        f.write(img)
    return 'img.jpg'

def CutImg(img, img_crop_path):
    img = array(img.convert('L').point(lambda x: 255 if x > 112 else 0))
    Im.fromarray(img).save('img_clean.jpg')
    img = Im.open('img_clean.jpg')
    if not os.path.exists(img_crop_path):
        os.makedirs(img_crop_path)
    for j in range(4):
        img_crop = img.crop((3 + j * 10, 4, 12 + j * 10, 16))
        img_crop.save(img_crop_path + 'img_clean' + str(j) + ".jpg")

def Predict(img_crop_path, model):
    character_list = ['1', '2', '3', 'b', 'c', 'm', 'n', 'v', 'x', 'z']
    img_names = os.listdir(img_crop_path)
    str1 = ''
    for img_name in img_names:
        img_np = np.array(Im.open(img_crop_path + img_name))
        v = img_np.reshape(img_np.shape[0] * img_np.shape[1], 1)
        v = v / 255
        pre = model.predict(v.T)
        max = 0
        p = -1
        for i in range(0, 10):
            if pre[0, i] > max:
                max = pre[0, i]
                p = i
        str1 = str1 + character_list[p]
    return str1

def main(model, img_path, img_crop_path):
    CutImg(Im.open(img_path), img_crop_path)
    str1 = Predict(img_crop_path, model)
    return str1

model = load_model("PredictModel.h5")
img_path = DownImg("http://csujwc.its.csu.edu.cn/verifycode.servlet")
img_crop_path = 'predeal/'
root = tk.Tk()
strVar = tk.StringVar()
str1 = main(model, img_path, img_crop_path)
strVar.set(str1)

root.title('中南大学教务系统验证码识别')
frame1 = Frame(root)
frame2 = Frame(root)
img = Im.open('img.jpg')
photo=ImageTk.PhotoImage(img)
imgLabel = Label(
    frame1,
    image = photo
)

def callback():
    img_path = DownImg("http://csujwc.its.csu.edu.cn/verifycode.servlet")
    img = Im.open('img.jpg')
    photo = ImageTk.PhotoImage(img)
    imgLabel.config(image = photo)
    imgLabel.image = photo
    str1 = main(model, img_path, img_crop_path)
    strVar.set(str1)

txtLabel = Label(
    frame1,
    textvariable = strVar
)
btnLabel = Button(
    frame2,
    text = '执行',
    command = callback
)
imgLabel.pack(side = tk.LEFT)
txtLabel.pack(side = tk.RIGHT)
btnLabel.pack()
frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)
mainloop()