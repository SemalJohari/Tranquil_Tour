import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cities = pd.read_csv('C:/Users/admin/Desktop/ML Project/data/Cities.csv', sep=",", header=0, encoding='latin-1')

cities['Tag2'] = ['Leisure', 'Leisure', 'Religious', 'Historical', 'Historical', 'Leisure', 'Leisure', 'Historical', 'Historical',
                 'Religious', 'Hilly', 'Leisure', 'Beaches', 'Leisure', 'Leisure', 'Beaches']
cities['Tourism_Rank'] = [32, 16, 17, 30, 19, 20, 6, 25, 24, 36, 9, 15, 36, 18, 37, 35]
cities['Tourism_ID'] = [3, 2, 2, 5, 4, 2, 1, 5, 5, 3, 4, 2, 5, 2, 1, 5]

cities_pivot = cities.pivot_table(columns=['Tag'], index='City', values='Tourism_ID')
cities_pivot.fillna(0, inplace=True)

from scipy.sparse import csr_matrix

cities_sparse = csr_matrix(cities_pivot)

from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(algorithm='brute')
model.fit(cities_sparse)

distance, suggestion = model.kneighbors(cities_pivot.iloc[15,:].values.reshape(1,-1), n_neighbors=6)

for i in range(len(suggestion)):
    print(cities_pivot.index[suggestion[i]])

cities_names = cities_pivot.index

import pickle
pickle.dump(model, open('artifacts/model.pkl', 'wb'))
pickle.dump(cities_names, open('artifacts/cities_names.pkl', 'wb'))
pickle.dump(cities, open('artifacts/cities.pkl', 'wb'))
pickle.dump(cities_pivot, open('artifacts/cities_pivot.pkl', 'wb'))

def recommend_cities(city_name):
    city_id = np.where(cities_pivot.index == city_name)[0][0]
    distance, suggestion = model.kneighbors(cities_pivot.iloc[city_id,:].values.reshape(1,-1), n_neighbors=6)
    
    recommended_cities = []
    for i in range(len(suggestion)):
        city = cities_pivot.index[suggestion[i]]
        for j in city:
            city_url = f"/city/{j}"
            recommended_cities.append((j, city_url))

    return recommended_cities        

city_name = input("Enter a city name: ")
recommend_cities(city_name)