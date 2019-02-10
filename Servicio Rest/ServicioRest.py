# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:54:37 2019

@author: Bryan
"""

from flask import Flask, jsonify
#from flask import Flask, request jsonify
import csv
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.externals import joblib
from sklearn import preprocessing



app = Flask(__name__)


@app.route('/prediccion/<task_id>', methods=['GET'])
def prediccion(task_id):
    print("VARIABLE TASK")
    print(task_id)
    editada = task_id[1:-1]
    
    print("VARIABLE Editada")
    print (editada)
    
    cadenallegada = editada.split(",")
    print("VARIABLE cadenallegada  ")
    a=int(float(cadenallegada[0]))
    b=int(float(cadenallegada[1]))
    c=int(float(cadenallegada[2]))
    d=int(float(cadenallegada[3]))
    e=int(float(cadenallegada[4]))
    f=int(float(cadenallegada[5]))
    g=int(float(cadenallegada[6]))
    h=int(float(cadenallegada[7]))
    print (a,b,c,d,e,f,g,h)
    

    myList = [a,b,c,d,e,f,g,h]
    with open('D:/Prueba/Creados/archivo.csv', 'a', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(myList)
        
    info = pd.read_csv('D:/Prueba/Creados/archivo.csv',
                  names = ["Tipo","Entidad",
                           "Sexo","Edad","Mes Ingreso","Etnia","Dia Ingreso",
                           "Especialidad"])



    features = ["Tipo","Entidad",
                           "Sexo","Edad","Mes Ingreso","Etnia","Dia Ingreso",
                           "Especialidad"]
    
    x = info.loc[:, features].values

    pca = PCA(n_components=4)

    principalComponents = pca.fit_transform(x)

    mj = joblib.load('D:/Prueba/Modelo 50/modelo65.pkl')
    datos = pd.read_csv('D:/Prueba/Creados/archivo.csv',names = ["Tipo","Entidad",
                           "Sexo","Edad"])


    scaler = StandardScaler()


    normalized_X = preprocessing.normalize(datos)


# Fit only to the training data
    scaler.fit(datos)
    datos = scaler.transform(datos)

    y = mj.predict(datos)
    print ("//////////////////////////////////////////////////////////////////")
    print(mj.score)
    print ("//////////////////////////////////////////////////////////////////")
    z = y[-1]
    print (y[-1])
    mm = z.tolist()
    
    print ("*******************************************************************")
    print ("  ***************************************************************  ")
    print ("    ***********************************************************    ")
    print ("        ***************************************************        ")
    print ("                ***********************************                ")
    print ("                    ***************************                    ")
    print ("                        *******************                        ")
    print ("                            ***********                            ")
    print ("                                ***                                ")
    print ("                                 *                                 ")
    return jsonify({'Value': mm})
    
     







@app.route('/clasificacionArbol/<task_id>', methods=['GET'])
def clasificacionArbol(task_id):
    print("VARIABLE TASK")
    print(task_id)
    editada = task_id[1:-1]
    
    print("VARIABLE Editada")
    print (editada)
    
    cadenallegada = editada.split(",")
    print("VARIABLE cadenallegada  ")
    a=int(float(cadenallegada[0]))
    b=int(float(cadenallegada[1]))
    c=int(float(cadenallegada[2]))
    d=int(float(cadenallegada[3]))
    e=int(float(cadenallegada[4]))
    f=int(float(cadenallegada[5]))
    g=int(float(cadenallegada[6]))
    print (a,b,c,d,e,f,g)
    

    myList = [a,b,c,d,e,f,g]

    with open('D:/Prueba/Clasificacion/archivo.csv', 'a', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(myList)


    info = pd.read_csv('D:/Prueba/Clasificacion/archivo.csv')

    print ("Entre")
    mj = joblib.load('D:/Prueba/Tensor/Arboles De Decision/Arboles0.93.pkl')

    y = mj.predict(info)
    z = y[-1]
    print (y[-1])
    print ("*******************************************************************")
    print ("  ***************************************************************  ")
    print ("    ***********************************************************    ")
    print ("        ***************************************************        ")
    print ("                ***********************************                ")
    print ("                    ***************************                    ")
    print ("                        *******************                        ")
    print ("                            ***********                            ")
    print ("                                ***                                ")
    print ("                                 *                                 ")
    return jsonify({'1': z})







@app.route('/clasificacionMaquinaSoporteVectorial/<task_id>', methods=['GET'])
def clasificacionMaquinaSoporteVecto(task_id):
    print("VARIABLE TASK")
    print(task_id)
    editada = task_id[1:-1]
    
    print("VARIABLE Editada")
    print (editada)
    
    cadenallegada = editada.split(",")
    print("VARIABLE cadenallegada  ")
    a=int(float(cadenallegada[0]))
    b=int(float(cadenallegada[1]))
    c=int(float(cadenallegada[2]))
    d=int(float(cadenallegada[3]))
    e=int(float(cadenallegada[4]))
    f=int(float(cadenallegada[5]))
    g=int(float(cadenallegada[6]))
    print (a,b,c,d,e,f,g)
    

    myList = [a,b,c,d,e,f,g]

    with open('D:/Prueba/Clasificacion/archivo.csv', 'a', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(myList)


    info = pd.read_csv('D:/Prueba/Clasificacion/archivo.csv')


    mj = joblib.load('D:/Prueba/Tensor/Maquinas De Soporte Vectorial/VectorMachine_0.85.pkl')

    y = mj.predict(info)
    z = y[-1]
    print (y[-1])
    print ("*******************************************************************")
    print ("  ***************************************************************  ")
    print ("    ***********************************************************    ")
    print ("        ***************************************************        ")
    print ("                ***********************************                ")
    print ("                    ***************************                    ")
    print ("                        *******************                        ")
    print ("                            ***********                            ")
    print ("                                ***                                ")
    print ("                                 *                                 ")
    return jsonify({'2': z})


@app.route('/clasificacionRegresionLogistica/<task_id>', methods=['GET'])
def clasificacionRegresionLogistica(task_id):
    print("VARIABLE TASK")
    print(task_id)
    editada = task_id[1:-1]
    
    print("VARIABLE Editada")
    print (editada)
    
    cadenallegada = editada.split(",")
    print("VARIABLE cadenallegada  ")
    a=int(float(cadenallegada[0]))
    b=int(float(cadenallegada[1]))
    c=int(float(cadenallegada[2]))
    d=int(float(cadenallegada[3]))
    e=int(float(cadenallegada[4]))
    f=int(float(cadenallegada[5]))
    g=int(float(cadenallegada[6]))
    print (a,b,c,d,e,f,g)
    

    myList = [a,b,c,d,e,f,g]

    with open('D:/Prueba/Clasificacion/archivo.csv', 'a', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(myList)


    info = pd.read_csv('D:/Prueba/Clasificacion/archivo.csv')


    mj = joblib.load('D:/Prueba/Tensor/Regresion Logística/LogReg_0.83.pkl')

    y = mj.predict(info)
    z = y[-1]
    print (y[-1])
    print ("*******************************************************************")
    print ("  ***************************************************************  ")
    print ("    ***********************************************************    ")
    print ("        ***************************************************        ")
    print ("                ***********************************                ")
    print ("                    ***************************                    ")
    print ("                        *******************                        ")
    print ("                            ***********                            ")
    print ("                                ***                                ")
    print ("                                 *                                 ")
    return jsonify({'3': z})






@app.route('/clasificacionVecinosCercanos/<task_id>', methods=['GET'])
def clasificacionVecinosCercanos(task_id):
    print("VARIABLE TASK")
    print(task_id)
    editada = task_id[1:-1]
    
    print("VARIABLE Editada")
    print (editada)
    
    cadenallegada = editada.split(",")
    print("VARIABLE cadenallegada  ")
    a=int(float(cadenallegada[0]))
    b=int(float(cadenallegada[1]))
    c=int(float(cadenallegada[2]))
    d=int(float(cadenallegada[3]))
    e=int(float(cadenallegada[4]))
    f=int(float(cadenallegada[5]))
    g=int(float(cadenallegada[6]))
    print (a,b,c,d,e,f,g)
    

    myList = [a,b,c,d,e,f,g]

    with open('D:/Prueba/Clasificacion/archivo.csv', 'a', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(myList)


    info = pd.read_csv('D:/Prueba/Clasificacion/archivo.csv')


    mj = joblib.load('D:/Prueba/Tensor/Vecinos mas cercanos/VecinosNumVec3-0.87.pkl')

    y = mj.predict(info)
    z = y[-1]
    print (y[-1])
    print ("*******************************************************************")
    print ("  ***************************************************************  ")
    print ("    ***********************************************************    ")
    print ("        ***************************************************        ")
    print ("                ***********************************                ")
    print ("                    ***************************                    ")
    print ("                        *******************                        ")
    print ("                            ***********                            ")
    print ("                                ***                                ")
    print ("                                 *                                 ")
    return jsonify({'4': z})



@app.route('/', methods=['GET'])
def index():
    return jsonify({'Value': "Hello, World!"})


if __name__ == '__main__':
     app.run(port='1234')