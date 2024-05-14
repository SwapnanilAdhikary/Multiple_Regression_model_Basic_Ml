# -*- coding: utf-8 -*-
"""Multiple_Linear_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-EdJz_iIRe7dTe0GLEoGOmuZ67iFg4d1
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('50_Startups.csv')
dataset.head()

dataset.tail()

X = dataset.iloc[:,:-1]
Y = dataset.iloc[:, -1].values
dataset.tail()

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder = 'passthrough')
X = np.array(ct.fit_transform(X))
#ColumnTransformer: This is a utility provided by scikit-learn for applying different transformations to different columns of a dataset.
#transformers=[('encoder', OneHotEncoder(), [3])]: Here, you are specifying a transformation for the columns in the dataset. It looks like you are applying a one-hot encoding transformation (OneHotEncoder) to the column at index 3 ([3]).
#This means that the values in this column will be converted into binary vectors representing categories.
#remainder='passthrough': This parameter specifies that any columns not specified in the transformers list should be left unchanged. In this case, it indicates that columns other than column 3 should remain unchanged.
#X = np.array(ct.fit_transform(X)): This line applies the transformations specified by the ColumnTransformer to the input data X. fit_transform() method fits the transformer to the data and then transforms it. Finally, np.array() is used to convert the transformed data into a NumPy array.

X

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

Y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Real values':Y_test,'Predicted values':Y_pred})
df

#rmse
from sklearn import metrics
print(np.sqrt(metrics.mean_squared_error(Y_test,Y_pred)))

