from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import random

def review(s,rating):
    star54= ['Excellent','fabulous','awesome','best book','very good','interesting','nice','attractive book']
    star3= ['good','ok','can do better','not bad']
    star21= ['bad','very boring','bad quality book']
    if s is NaN:
        if rating>=4 and rating<=5:
            return random.choice(star54)
        if rating>=1 and rating<=2:
            return random.choice(star21)
        
        return random.choice(star3)
    else:
        return s


df= pd.read_excel('br.xlsx')
c=0
x=[]
for i in range(5400):
    #print(type(df.iloc[i]['reviews']))
    if df.iloc[i]['reviews'] is NaN:
        #print(type(df.iloc[i]['reviews']))
        x.append(review(df.iloc[i]['reviews'],df.iloc[i]['rating']))
    else:
        x.append(df.iloc[i]['reviews'])
bookid= df['book_id']
title= df['title']
userid= df['user_id']
rating= df['rating']
rev= pd.Series(x)
d= {'book_id':bookid,'title':title,'user_id':userid,'rating':rating,'review':rev}
data= pd.DataFrame(d)
data.to_csv('books-data.csv',encoding='utf-8',index=False)