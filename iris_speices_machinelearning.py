# -*- coding: utf-8 -*-
"""Pratyush_Kumar__Patra.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JK3I4NgfsKeSOcQdOe7fCNxMqGYoo7i2
"""

import pandas as pd
import numpy as np
!pip install scikit-learn

from  sklearn.datasets import load_iris
iris_dataset=load_iris()

from  sklearn.datasets import load_iris
iris_dataset=load_iris()

from  sklearn.datasets import load_iris
iris_dataset=load_iris()

print("Keys of iris dataset: \n{}".format(iris_dataset.keys()))

print(iris_dataset['DESCR'][:193]+"n.....")

print("Target names: {}".format(iris_dataset['target_names']))

print("feature_names: {}".format(iris_dataset['feature_names']))

print("Type of data: {}".format(type(iris_dataset['data'])))

print("Shape of data: {}".format(iris_dataset['data'].shape))

print("First five rows of data:\n{}".format(iris_dataset['data'][:5]))

print("Target:\n{}".format(iris_dataset['target']))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))
print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

from sklearn.neighbors import KNeighborsClassifier
pnn= KNeighborsClassifier(n_neighbors=1)

pnn.fit(X_train,y_train)

X_new=np.array([[5,2.9,1,0.2]])
print("X_new.shape: {}".format(X_new.shape))

prediction = pnn.predict(X_new)
print("Prediction: {}".format(prediction))
print("Prediction target name: {}".format(iris_dataset['target_names'][prediction]))

y_pred = pnn.predict(X_test)
print("Test Set predictions:\n {}".format(y_pred))

print("Test set score: {}".format(np.mean(y_pred == y_test)))



