# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F2eKCxT-tn_JhaMI5o-VYpfkwC5FtNaD
"""

import numpy as np
import pandas as pd
import tensorflow as tf

tf.__version__

"""Load the Dataset"""

dataset = pd.read_csv('/content/Churn_Modelling.csv')

dataset.head(10)

X = dataset.iloc[:, 3:-1]
y = dataset.iloc[:, -1]

print(X)

print(y)

"""Checking for null values"""

X.isnull().count

y.isnull().count

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(X.iloc[:, 3:])
X.iloc[:, 3:] = imputer.transform(X.iloc[:, 3:])

print(X)

"""Encoding categorical Data"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X.iloc[:, 2] = le.fit_transform(X.iloc[:,2])

print(X)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
c = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[1])], remainder= 'passthrough')
X = np.array(c.fit_transform(X))

print(X)



"""Splitting the dataset into training and test"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state= 0)

"""Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform (X_train)
X_test = sc.transform(X_test)

"""#Building ANN

###Initializing ANN
"""

ann = tf.keras.models.Sequential()

"""Adding input layer and 1st hidden layer"""

ann.add(tf.keras.layers.Dense(units= 6, activation="relu"))

"""Adding second hidden layer"""

ann.add(tf.keras.layers.Dense(units=6, activation= "relu"))

"""Adding the output layer"""

ann.add(tf.keras.layers.Dense(units=1, activation= "sigmoid"))

"""#Training the ANN

Compiling
"""

ann.compile(optimizer= "adam", loss= "binary_crossentropy", metrics= ["accuracy"])

ann.fit(X_train, y_train, batch_size= 32, epochs=100)

y_pred = ann.predict(X_test)
print(y_pred)

