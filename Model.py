# -*- coding: utf-8 -*-
"""
Created on Mon May 30 21:53:46 2022

@author: abdul
"""

import pandas as pd
dataset = pd.read_csv("PAkwheels_Clean.csv")



X = dataset.iloc[:, 1:]
y = dataset.iloc[:, :1]


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X, y)

import pickle
pickle.dump(regressor, open('Regressor_prie_prediction.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('Regressor_prie_prediction.pkl','rb'))

data_unseen = pd.read_csv('Data_Unseen.csv') 
data_unseen.shape

print(model.predict(data_unseen))




