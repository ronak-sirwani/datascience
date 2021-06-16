from numpy import random
import pandas as pd
import numpy as np
from pandas.core.series import Series
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import re

dataset= pd.read_csv('train.csv')

# droping those features which do not contribute to survival
dataset= dataset.drop(['PassengerId','Ticket','Name'],axis=1)


# creating two more features
# 1. relatives = SibSp+parch
# 2. individual= yes=1 / no=1

dataset['relatives']= dataset['SibSp']+dataset['Parch']
dataset.loc[dataset['relatives'] > 0, 'individual']= 0
dataset.loc[dataset['relatives'] == 0, 'individual']= 1
dataset['individual']= dataset['individual'].astype(int)

# converting cabin names into numerical 
# according to their alphabetical order 
# e.g a/A=1,b/B=2

alpha= {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7}

dataset['Cabin']= dataset['Cabin'].fillna('u0')
dataset['newCabin']= dataset['Cabin'].map(lambda x: re.compile("([a-zA-Z]+)").search(x).group())
dataset['newCabin']= dataset['newCabin'].map(alpha)
dataset['newCabin']= dataset['newCabin'].fillna(0)
dataset['newCabin']= dataset['newCabin'].astype(int)

dataset= dataset.drop(['Cabin'],axis=1)

# filling empty rows in age column
# with mean of all ages

fill_value= dataset['Age'].mean(skipna=True)
dataset['Age']=dataset['Age'].fillna(fill_value)
dataset['Age']= dataset['Age'].astype(int)

# convert age into different intervals
dataset.loc[dataset['Age'] <=16, 'Age']=0
dataset.loc[(dataset['Age'] >16) & (dataset['Age'] <=32), 'Age']=1
dataset.loc[(dataset['Age'] >32) & (dataset['Age'] <=48), 'Age']=2
dataset.loc[(dataset['Age'] >48) & (dataset['Age'] <=64), 'Age']=3
dataset.loc[dataset['Age'] >64, 'Age']=4
# filling empty rows in embarked
# by their most occuring value

most_occur= 'S'
dataset['Embarked']= dataset['Embarked'].fillna(most_occur)
embark= {'S':1,'C':2,'Q':3}
dataset['Embarked']= dataset['Embarked'].map(embark)

# converting fare float value to int 
#and 0 to empty rows

dataset['Fare']= dataset['Fare'].astype(int)
dataset['Fare']= dataset["Fare"].fillna(0)
#print(dataset['Fare'].describe())

# converting gender values into integers

gender= {'male':0,'female':1}
dataset['Gender']= dataset['Gender'].map(gender)


target= dataset['Survived']
dataset= dataset.drop(['Survived','SibSp','Parch'],axis=1)

X_train,X_test,y_train,y_test= train_test_split(dataset,target,test_size= 0.30,random_state=42)

print("Final dataset: ")
print(dataset.head(10))

for i in range(1,7):
    model= DecisionTreeClassifier(max_depth=i,splitter='best')
    model.fit(X_train,y_train)
    y_predict= model.predict(X_test)
    
    print("Accuracy for depth {}:".format(i),metrics.accuracy_score(y_test,y_predict)*100)