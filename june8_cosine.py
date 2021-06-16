import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

df= pd.read_csv('movie-ratings.csv')
data= df.fillna(0)
print(data)
print(data.pivot(index=['userid']))
print("Cosine similarity :")
sm= cosine_similarity(data)
print(sm)

print(data.iloc[1])

