import pandas as pd
"""
# to create series use list, dictionary
# ndarray and other iterable
a= pd.Series([1,2,3,4,5])
print(a)
"""
# to create dataframe use dictionary,series,
# list and other iterables
d1= {'a':1,'b':2,'c':3}
data= pd.DataFrame(d1,index=[0])
print(data)