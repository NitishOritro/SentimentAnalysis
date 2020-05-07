# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

excel_file = "Restaurant.xlsx"


dataset2 = pd.read_excel("TransPosedataValue.xlsx")

X = pd.DataFrame(dataset2.iloc[:, :].values).to_numpy()

dataset = pd.read_excel(excel_file, encoding="utf-8", usecols="E")

y = pd.DataFrame(dataset.iloc[:, :].values).to_numpy()

#Splitting the dataset into Training and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
  
#Fitting Naive Bayes to The Training Set

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

#Predicting the test set results
y_pred = classifier.predict(X_test)


y_test_list = y_test.tolist()
y_pred_list = y_pred.tolist()

y_pred_new = []
y_test_new = []

for i in range(len(y_test_list)):
    if y_test[i] != 0:
        y_pred_new.append(y_pred_list[i])
        y_test_new.append(y_test_list[i])

plus = 0
minus = 0
for i in range(len(y_test_new)):
    if(y_test_new[i][0] == 1):
        plus += 1
    else:
        minus += 1
        
print(plus)
print(minus)
    
for i in range(len(y_pred_new)):
    if y_pred_new[i] != 0:
       y_pred_new[i] = -1
        
y_pred_new_np = np.array(y_pred_new)
y_test_new_np = np.array(y_test_new)



#Making Cofusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test_new_np, y_pred_new_np)





