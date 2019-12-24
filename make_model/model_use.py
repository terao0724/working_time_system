import time
import cv2
import os
import re
import keras
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.preprocessing.image import array_to_img, img_to_array, load_img, random_rotation
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import model_from_json

model = model_from_json(open('face_study_model.json').read())
model.load_weights('face_study_model.h5')
model.compile(loss='categorical_crossentropy', optimizer='SGD', metrics=['accuracy'])
img = img_to_array(load_img('./answer/yozo869.jpg', target_size=(50,50)))
a = 0
X = np.asarray(img)
X = X.astype('float32')
X = X / 255.0
pred_label = model.predict_proba(np.array([X]), batch_size=1, verbose=0)
print(pred_label[0])
for c in pred_label[0]:
    if c > 0.98:
        a = 1
if a == 1:
    pred_label2 = model.predict_classes(np.array([X]), batch_size=1, verbose=0)
    number_dict = {0: "apple", 1: "grape"}
    a = int(pred_label2)
    b = number_dict[a]
    print(b + "です")
    a = 0
else:
    print("データが登録されていません")

