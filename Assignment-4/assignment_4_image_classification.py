# -*- coding: utf-8 -*-
"""Assignment_4_Image_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/mayankp158/59739353e025b82d362ebf0350245ff5/assignment_4_image_classification.ipynb

First run the following cells to import current version of Tensorflow.
"""

# Commented out IPython magic to ensure Python compatibility.
try:
  # %tensorflow_version only exists in Colab.
#   %tensorflow_version 2.x
except Exception:
  pass

from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.utils import np_utils

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

"""## Import the Image dataset

In this notebook, we are going to classify images from the [MNIST](http://yann.lecun.com/exdb/mnist/) dataset. 


<table>
  <tr><td>
    <img src="https://miro.medium.com/max/479/1*yBdJCRwIJGoM7pwU-LNW6Q.png"
         alt="CIFAR samples"  >
  </td></tr>
  <tr><td align="center">
    <b>Figure 1.</b> <a href="http://yann.lecun.com/exdb/mnist/">MNIST samples</a>.<br/>&nbsp;
  </td></tr>
</table>
"""

tf.random.set_seed(100)
mnist = keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

num_train, img_rows, img_cols =  train_images.shape
num_test, _, _ =  test_images.shape
num_classes = len(np.unique(train_labels))

"""## Explore the data

#### Q1: What is the shape of train and test data in MNIST dataset?
"""

# write your code here to answer above question
train_images.shape
test_images.shape

"""## Preprocess the data

The data must be preprocessed before training the network.
"""

train_images = train_images / 255.0
test_images = test_images / 255.0

"""## Build the model

Model should contain following layers:
  
  Flatten(Input) -> Dense(10, activation='softmax')
  
Use 'Adam' optimizer

Use 'accuracy' as your metric

#### Q2: Which loss function would be appropriate here?
"""

# Build and compile your model in this cell. Make sure to first answer Q2.
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(300, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

"""#### Q3: Total number of **parameters**?

## Train the model

Run the following command to train your model:
"""

history = model.fit(train_images, train_labels, batch_size=512, validation_data = (test_images, test_labels), epochs=10)

"""Run the above command before answering Q4.

Modify the model and run the above code answer Q5.

## Test Underfitting and Overfitting
"""

# summarize history for accuracy
def plot_acc(history):
  plt.plot(history.history['accuracy'])
  plt.plot(history.history['val_accuracy'])
  plt.title('model accuracy')
  plt.ylabel('accuracy')
  plt.xlabel('epoch')
  plt.legend(['train', 'test'], loc='upper left')
  plt.show()
# summarize history for loss
def plot_loss(history):
  plt.plot(history.history['loss'])
  plt.plot(history.history['val_loss'])
  plt.title('model loss')
  plt.ylabel('loss')
  plt.xlabel('epoch')
  plt.legend(['train', 'test'], loc='upper left')
  plt.show()

plot_acc(history)
plot_loss(history)