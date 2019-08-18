import os
from PIL import Image
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

def Construct_Set(n, kind = 'train'):
    X_set = np.zeros((n, 1))
    character_list = ['1', '2', '3', 'b', 'c', 'm', 'n', 'v', 'x', 'z']
    Y_set = np.zeros((10, 1))
    for i in range(0, 10):
        img_path = kind + '_set/' + character_list[i] + '/'
        images_name = os.listdir(img_path)
        cnt = 0
        for img_name in images_name:
            img = np.array(Image.open(img_path + img_name))
            v = img.reshape(img.shape[0] * img.shape[1], 1)
            v = v / 255
            X_set = np.c_[X_set, v]
            cnt = cnt + 1
        Y_img = np.zeros((10, cnt))
        Y_img[i, :] = 1
        Y_set = np.c_[Y_set, Y_img]
    X_set = np.delete(X_set, 0, axis=1)
    Y_set = np.delete(Y_set, 0, axis=1)
    return X_set, Y_set

X_train, Y_train = Construct_Set(108, 'train')
X_test, Y_test = Construct_Set(108, 'test')
print(X_train)
print(X_train.shape)
print(Y_train)
print(Y_train.shape)
print(X_test)
print(X_test.shape)
print(Y_test)
print(Y_test.shape)

model = Sequential()

model.add(Dense(108, activation='relu', input_dim=108))
model.add(Dense(81, activation='relu'))
model.add(Dense(54, activation='relu'))
model.add(Dense(36,activation='relu'))
model.add(Dense(27,activation='relu'))
model.add(Dense(10,activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd')
model.fit(X_train.T, Y_train.T,
          epochs=1000,
          batch_size=128)
score = model.evaluate(X_test.T, Y_test.T, batch_size=16)
print(score)

model.summary()
model.save("PredictModel.h5")