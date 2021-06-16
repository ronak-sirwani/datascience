from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data= pd.read_csv('sales.csv')
col1= np.array(data[['month','sales']])
col2= np.array(data['profit'])

X_train,X_test,y_train,y_test= train_test_split(col1,col2,test_size= 0.2,random_state=1)
model= LinearRegression()
model.fit(X_train,y_train)

pd.to_pickle(model,'sales_model.pickle')