from re import T
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
sentences= ['Python for data science','Python for machine learning','Python for big data']

vector= TfidfVectorizer()
vector.fit(sentences)
transform= vector.transform(sentences)
df= pd.DataFrame(transform.toarray(),columns= vector.get_feature_names())
print(df)
print(vector.vocabulary_)
print(vector.idf_)
print(transform.shape)
