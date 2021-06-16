import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from textblob import TextBlob
from textblob.en import polarity
from textblob.tokenizers import word_tokenize


stop_words = set(stopwords.words('english'))
def find_polarity(review):
    global stop_words

    blob= TextBlob(review)
    words= blob.words
    sentence= [word for word in words if word not in stop_words]
    sent= " ".join(sentence)   
    blob2= TextBlob(sent)
    
    return blob2.sentiment.polarity

data= pd.read_csv('cloths-rating.csv')

apply_functions= {'Rating': 'mean', 'Text': lambda x: ".".join(x)}

new_data= data.groupby(['ProductID']).aggregate(apply_functions)

new_data['polarity']= new_data['Text'].apply(find_polarity) 
new_data.loc[new_data['polarity'] > 0,'sentiment']= 'Positive'
new_data.loc[(new_data['polarity'] ==0),'sentiment']= 'Neutral'
new_data.loc[new_data['polarity'] < 0,'sentiment']= 'Negative'

print(new_data.head())