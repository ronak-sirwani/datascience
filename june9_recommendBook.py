import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn import neighbors
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

# Dataframe of books data
data= pd.read_csv('book-ratings.csv')
print(data.info())
# Creating pivot table from dataframe
data_pivot= data.pivot_table(index='book_id',columns='user_id',values='rating').fillna(0)

# creating csr matrix of rating values
data_pivot_matrix= csr_matrix(data_pivot.values)

# buliding model for recommender system
model= NearestNeighbors(metric='cosine')
model.fit(data_pivot_matrix)

# list of book id
data_index= list(data_pivot.index)
book_id= int(input("Enter book id: "))
num= int(input("No. of recommendations (max=10): "))

# finding index of book entered
book_id_index= data_index.index(book_id)

# distance from the given book (in increasing order)
# indices of recommended boks
distance,indices = model.kneighbors(data_pivot.iloc[book_id_index,:].values.reshape(1,-1),n_neighbors=num+1)

# converting distance and indices into 1-D array
dist= distance.reshape(-1)
ind= indices.reshape(-1)

# dictionary for storing distance values of recommended books from given book
recommend_data= dict()
lst=[]
for i in range(1,len(dist)):
    bid= data_pivot.index[ind[i]]
    recommend_data[str(bid)]= float(dist[i])
    print("Distance of book with id {} with respect to book with id {} = {}".format(bid,book_id,recommend_data[str(bid)]))
    lst.append(data.loc[data['book_id']==bid]['title'].values[0])

print("Dictionary with similarity distance: \n",recommend_data)

print("Top {} recommendations for readers of book: {} ".format(num,data.loc[data['book_id']==book_id]['title'].values[0]))

print("Books recommended are: ")
print("\n".join(lst))