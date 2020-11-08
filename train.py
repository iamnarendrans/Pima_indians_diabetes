# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:12:16 2020

@author: kiddy
"""

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
x = dataset[:,0:8]
y = dataset[:,8]

model = Sequential()
model.add(Dense(12,input_dim = 8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x, y,epochs=100, batch_size=10)
_, accuracy = model.evaluate(x,y)
print('Accuracy: %.2f' %(accuracy * 100))


model_json = model.to_json()
with open("model_json","w")as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Model saved to the disk")