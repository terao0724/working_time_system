#import time
#import cv2
import os
import re
import keras
from keras.utils import np_utils
from keras import optimizers
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.preprocessing.image import array_to_img, img_to_array, load_img, random_rotation
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def list_pictures(directory, ext='jpg|jpeg|bmp|png|ppm'):
    return [os.path.join(root, f)
            for root, _, files in os.walk(directory) for f in files
            if re.match(r'([\w]+\.(?:' + ext + '))', f.lower())]

X = []
Y = []
for picture in list_pictures('./apple/'):
    img = img_to_array(load_img(picture, target_size=(100,100)))
    X.append(img)
    Y.append(0)

for picture in list_pictures('./grape/'):
    img = img_to_array(load_img(picture, target_size=(100,100)))
    X.append(img)
    Y.append(1)
    
X = np.asarray(X)
Y = np.asarray(Y)
X = X.astype('float32')
X = X / 255.0
Y = np_utils.to_categorical(Y, 2)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.4, random_state = 111)

model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same',input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.5))

model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.5))

model.add(Flatten())

model.add(Dense(100000))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(2))       
model.add(Activation('softmax'))

sgd = optimizers.SGD(lr=0.009876, clipnorm=1.)
model.compile(loss='categorical_crossentropy', optimizer= sgd, metrics=['accuracy'])
model.save_weights('param.hdf5')
history = model.fit(X_train, y_train, batch_size=10, epochs=20, validation_data = (X_test, y_test), verbose = 1)
predict_classes = model.predict_classes(X_test)
mg_df = pd.DataFrame({'predict': predict_classes, 'class': np.argmax(y_test, axis=1)})
pd.crosstab(mg_df['class'], mg_df['predict'])
print("Adadelta")
