import os
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten, Dense, Dropout
from keras.utils import np_utils
import numpy as np
#from keras.layers.normalization import BatchNormalization
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from skimage import io
import pandas as pd
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#import matplotlib as mpl
#mpl.use('TkAgg')

# Get list of images.
directories = os.listdir('./')
images = []

with_pole_images = []
without_pole_images = []

for image_path in os.listdir('./hasStreetPole'):
  #print( image_path);
  if image_path.startswith('.') == True:
    continue;
  # create the full input path and read the file
  input_path = os.path.join('./hasStreetPole' , image_path)
  #print( image_path);
  img = io.imread(input_path, as_grey=True)
  img = img.reshape([600, 300, 1])
  with_pole_images.append(img)
x_train_with_pole = np.array(with_pole_images)
#df1=pd.Series(x_train_with_pole)
#print(len(df1))
#print(len(x_train_with_pole))
#print(x_train_with_pole.shape)
y_train_with_pole = np.full(len(x_train_with_pole), 1, dtype=int)
#print(y_train_with_pole.shape)
#print(y_train_with_pole)

for image_path in os.listdir('./noStreetPole'):
  #print( image_path);
  if image_path.startswith('.') == True:
    continue;
  # create the full input path and read the file
  input_path = os.path.join('./noStreetPole' , image_path)
  #print( image_path);
  img = io.imread(input_path, as_grey=True)
  img = img.reshape([600, 300, 1])
  without_pole_images.append(img)
x_train_without_pole = np.array(without_pole_images)
y_train_without_pole = np.full(len(x_train_without_pole), 0, dtype=int)


testHolder = np.vstack((x_train_with_pole, x_train_without_pole));
#print(x_train_with_pole.size)
#print(x_train_without_pole.size)
#print(testHolder.size)
# Split dataset in train and test.
#print('$$$$$')
#print(y_train_with_pole)
#print(y_train_without_pole)
#print('$$$$$$$')
testHolder2 = np.concatenate((y_train_with_pole, y_train_without_pole));
x_train, x_test, y_train, y_test = train_test_split(testHolder,
       testHolder2, test_size=0.2, random_state=1) 




model = Sequential()
#Conv2D is used for images Conv = https://en.wikipedia.org/wiki/Kernel_(image_processing)
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=[600, 300, 1]))
#model.add(BatchNormalization())
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#Flatten used to make it a (x,) array.
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))


# Compile model and tell it we only want a 0 or 1 output
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()


model.fit(x_train, y_train, batch_size=100, epochs=8, verbose=1)
#model.fit(x_train_without_pole, y_train_without_pole, batch_size=100, epochs=8, verbose=1)

prediction = model.predict(x_test)
pp = model.predict_proba(x_test)
print(pp)
print(prediction)
print(y_test)

prediction = model.predict(x_train)

print(prediction)
print(y_train)


