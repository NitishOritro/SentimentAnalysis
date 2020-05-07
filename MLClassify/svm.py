# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report, confusion_matrix
excel_file = "Restaurant\Restaurant.xlsx"


dataset2 = pd.read_excel("Restaurant\BiGramTransPoseDataRestaurant.xlsx")

X = pd.DataFrame(dataset2.iloc[:, :].values).to_numpy()

dataset = pd.read_excel(excel_file, encoding="utf-8", usecols="E")

y = pd.DataFrame(dataset.iloc[:, :].values).to_numpy()

#Splitting the dataset into Training and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#from sklearn.SVM import SVM kernel
classifier = svm.SVC(kernel='linear', C = 1.5, max_iter=600)
classifier.fit(X_train, y_train.ravel())
#Predicting the test set results
y_pred = classifier.predict(X_test)
#Making Cofusion Matrix
cmMain = confusion_matrix(y_test, y_pred)

#precision_SVM = (cm[2][2] / (cm[0][2] + cm[1][2] + cm[2][2])) * 100
#aa_SVM_precision = precision_score(y_test, y_pred, average='macro')
#SVM_recall = recall_score(y_test, y_pred, average='macro')
#SVM_fScore = f1_score(y_test, y_pred, average='macro')

SVM_accuracy_main = accuracy_score(y_test, y_pred)
report  = classification_report(y_test, y_pred, output_dict=True)
print(classification_report(y_test, y_pred))


print(cmMain)


###################### OUR Data """""""""""""""""""""""""


dataset = pd.read_excel(excel_file, encoding="utf-8", usecols="I")

y = pd.DataFrame(dataset.iloc[:, :].values).to_numpy()

#Splitting the dataset into Training and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#from sklearn.SVM import SVM kernel
classifier = svm.SVC(kernel='linear', C = 1.5, max_iter=600)
classifier.fit(X_train, y_train.ravel())
#Predicting the test set results
y_pred = classifier.predict(X_test)
#Making Cofusion Matrix
cm = confusion_matrix(y_test, y_pred)

#precision_SVM = (cm[2][2] / (cm[0][2] + cm[1][2] + cm[2][2])) * 100
aa_SVM_precision = precision_score(y_test, y_pred, average='weighted')
#SVM_recall = recall_score(y_test, y_pred, average='macro')
#SVM_fScore = f1_score(y_test, y_pred, average='macro')

SVM_accuracy_Test = accuracy_score(y_test, y_pred)
report  = classification_report(y_test, y_pred, output_dict=True)
print(classification_report(y_test, y_pred))
print("SVM_precision : "+str(aa_SVM_precision))
print("SVM_accuracy : "+str(SVM_accuracy_Test))

print(cm)




#df = pd.DataFrame(report).transpose()

#df.to_excel("C:\\Users\\Nitish Ranjan\\main-data\\SVM.xlsx", index=False)

######################################
######Logistic Regression ###########
classifier1 = LogisticRegression(C = 1, max_iter=3000, random_state=0)
classifier1.fit(X_train, y_train)
y_pred = classifier1.predict(X_test)

#Making Cofusion Matrix
cm1 = confusion_matrix(y_test, y_pred)

#precision_LR = (cm1[2][2] / (cm1[0][2] + cm1[1][2] + cm1[2][2])) * 100
ab_LR_precision = precision_score(y_test, y_pred, average='weighted')
LR_recall = recall_score(y_test, y_pred, average='macro')
LR_fScore = f1_score(y_test, y_pred, average='macro')

ab_LR_accuracy_ = accuracy_score(y_test, y_pred)


#########################################
## K Means Nearest Neighbors Classifier################

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)
cm2 = confusion_matrix(y_test, y_pred)

#precision_KNN = (cm2[2][2] / (cm2[0][2] + cm2[1][2] + cm2[2][2])) * 100

ac_KNN_precision = precision_score(y_test, y_pred, average='weighted')
KNN_recall = recall_score(y_test, y_pred, average='macro')
KNN_fScore = f1_score(y_test, y_pred, average='macro')

ac_KNN_accuracy_ = accuracy_score(y_test, y_pred)


##########################################
####### Random Forest Classifier ########
clf = RandomForestClassifier(max_depth=3, random_state=0)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
cm3 = confusion_matrix(y_test, y_pred)

#precision_RF = (cm3[2][2] / (cm3[0][2] + cm3[1][2] + cm3[2][2])) * 100

ad_RF_precision = precision_score(y_test, y_pred, average='weighted')
RF_recall = recall_score(y_test, y_pred, average='macro')
RF_fScore = f1_score(y_test, y_pred, average='macro')

ad_RF_accuracy_ = accuracy_score(y_test, y_pred)


##########################################
####### Naive  Classifier ########
clf = MultinomialNB()
clf.fit(X, y)


y_pred = clf.predict(X_test)
cm3 = confusion_matrix(y_test, y_pred)

#precision_RF = (cm3[2][2] / (cm3[0][2] + cm3[1][2] + cm3[2][2])) * 100

ae_NV_precision = precision_score(y_test, y_pred, average='weighted')
NV_recall = recall_score(y_test, y_pred, average='weighted')
NV_fScore = f1_score(y_test, y_pred, average='macro')

ae_NV_accuracy_ = accuracy_score(y_test, y_pred)

print(classification_report(y_test, y_pred))

print(cm3)
print("NV_accuracy_ : "+str(ae_NV_accuracy_))



#################Gaussian ###########
gnb = GaussianNB()
gnb.fit(X, y)
y_pred = gnb.predict(X_test)
cm4 = confusion_matrix(y_test, y_pred)

af_MNV_accuracy_ = accuracy_score(y_test, y_pred)

print(classification_report(y_test, y_pred))

print(cm4)
print("MNV_accuracy_ : "+str(af_MNV_accuracy_))






print("LR_accuracy : "+str(ab_LR_accuracy_))
print("KNN_accuracy : "+str(ac_KNN_accuracy_))
print("RF_accuracy_ : "+str(ad_RF_accuracy_))
print("NV_accuracy_ : "+str(ae_NV_accuracy_))
print("NV_accuracy_ : "+str(af_MNV_accuracy_))



print("LR_precision : "+str(ab_LR_precision))
print("KNN_precision : "+str(ac_KNN_precision))
print("RF_precision : "+str(ad_RF_precision))





"""
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')

"""
#cm = confusion_matrix(y_test_new_np, y_pred_new_np)



"""
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
"""



