# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 19:03:33 2019

@author: Bryan
"""


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pickle
from sklearn.decomposition import PCA as sklearnPCA



info = pd.read_csv('D:/Prueba/Data final csv no cabecera comas.csv',
                  names = ["Tipo","Entidad",
                           "Sexo","Edad","Mes Ingreso","Mes Egreso","Dia Egreso",
                           "Dias","Especialidad","DiasCat"])



features = ["Tipo","Entidad",
                           "Sexo","Edad","Mes Ingreso","Mes Egreso","Dia Egreso",
                           "Dias","Especialidad"]

# Separating out the features
x = info.loc[:, features].values

# Separating out the target
y = info.loc[:,['DiasCat']].values
z = info.loc[:,['Dias']].values

print ("Estandarizo")
# Standardizing the features
x = StandardScaler().fit_transform(x)
print ("***********************************************************************")

print (info)

print ("***********************************************************************")

pca = PCA(n_components=4)

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents
             , columns = ['Componente 1', 'Componente 2', 'Componente 3',
                          'Componente 4'])
finalA = pd.concat([principalDf, info[['Dias']]], axis = 1)
finalDf = pd.concat([finalA, info[['DiasCat']]], axis = 1)
print (finalDf)

finalDf.to_pickle('D:/Prueba/Prueba.pkl')

loaded_model = pickle.load(open('D:/Prueba/Prueba.pkl', 'rb'))
loaded_model.

