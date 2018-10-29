# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:14:37 2018

@author: user
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
Dataset = pd.read_csv('BreadBasket.csv')
Dataset.head()

sns.set(rc={'figure.figsize':(20,10)})
sns.set(font_scale=2)
print(Dataset['Item'].unique())
sns.countplot(Dataset['Item'],label="Time")
plt.show()
feature_names = ['Time']
X = Dataset[feature_names]
Y = Dataset['Item']
X_train, X_test, y_train, y_test = train_test_split(X, Y,train_size=0.65)


scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)





logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print('Accuracy of Logistic regression classifier on training set: {:.2f}'.format(logreg.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

pred = logreg.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))


# -------- Nearest Neighbors ----------
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of KNN regression classifier on training set: {:.2f}'.format(knn.score(X_train, y_train)))
print('Accuracy of KNN regression classifier on test set: {:.2f}'.format(knn.score(X_test, y_test)))

pred1 = knn.predict(X_test)
print(confusion_matrix(y_test, pred1))
print(classification_report(y_test, pred1))



# ------ SVM Classifier (Support Vector Machine, non-linear classification, unsupervised, non-probablistic)----------------
from sklearn.svm import SVC
svc1 = SVC()
svc1.fit(X_train, y_train)
print('Accuracy of svc regression classifier on training set: {:.2f}'.format(svc1.score(X_train, y_train)))
print('Accuracy of SVC regression classifier on test set: {:.2f}'.format(svc1.score(X_test, y_test)))

pred2 = svc1.predict(X_test)
print('Confusionnnnnnnnnnnn')
cm=confusion_matrix(y_test, pred2)
print(cm)

print(classification_report(y_test, pred2))


d=pd.read_csv("BreadBasket_DMS.csv")

Dataset = pd.read_csv('BreadBasket.csv')
Dataset.set_index(Dataset.iloc[:,-1],inplace=True)
#d['Time']=pd.to_datetime(d['Time'])
#type(d['Time'])
#plt.barplot(Dataset.iloc[:,0])
Dataset.describe()
Dataset.index


sns.set(rc={'figure.figsize':(10,10)})
sns.set(font_scale=2)
sns.swarmplot(x="Time",y="Item",data=Dataset)


