# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:23:20 2019

@author: Bryan
"""

# Import the needed libraries
import numpy as np  
import pandas as pd  
import tensorflow as tf  
import urllib.request as request  
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib




info = pd.read_csv('D:/Prueba/TENSOR.csv')


print (info.groupby('estadia_var').size())
print('Descripción del dataset:')
print(info.describe())
print(info.info())



X = np.array(info.drop(['estadia_var'], 1))
y = np.array(info['estadia_var'])

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
print('Son {} datos para entrenamiento y {} datos para prueba'.format(X_train.shape[0], X_test.shape[0]))
#Modelo de Vecinos más Cercanos
algoritmo = KNeighborsClassifier(n_neighbors=5)
algoritmo.fit(X_train, y_train)
Y_pred = algoritmo.predict(X_test)
print('Precisión Vecinos más Cercanos: {}'.format(algoritmo.score(X_train, y_train)))


r = format(algoritmo.score(X_train, y_train))[0:4]
joblib.dump(algoritmo, 'D:/Prueba/Tensor/Vecinos mas cercanos/Vecinos_'+r+'.pkl')
