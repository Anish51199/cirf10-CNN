# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:39:17 2020

@author: anish
"""

import keras
from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

#Analysis
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(20,5))
for i in range (36):
  ax=fig.add_subplots()