import pandas as pd
from pandas.core.algorithms import mode

model= pd.read_pickle('sales_model.pickle')

n= int(input("Enter no. of months: "))
for i in range(n):
    month= int(input("month no. : "))
    sales= int(input("Sales amount: "))
    res=model.predict([[month,sales]])
    print(res)