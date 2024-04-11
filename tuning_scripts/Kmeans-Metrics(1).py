#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import matplotlib.cm, matplotlib.colors
from sklearn import metrics
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets, manifold

from time import time
import time
import warnings
from itertools import cycle, islice

import matplotlib.gridspec as gridspec
from sklearn.cluster import OPTICS, cluster_optics_dbscan

from sklearn.cluster import BisectingKMeans, KMeans

from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split

from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingGridSearchCV

from sklearn.neighbors import NearestNeighbors

start_time = time.time()
data_3 = np.loadtxt('3N_forces_data.txt', delimiter='\t')

import numpy as np
from sklearn.cluster import KMeans, BisectingKMeans
from sklearn import metrics

# Number of cluster centers for KMeans and BisectingKMeans
n_clusters_list = [4, 6, 8]

# Algorithms to compare
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}

# Przygotowanie danych
X = data_3
random_state = 0

# Inicjalizacja tabeli do przechowywania wyników
results = []

# Pętle po algorytmach klastrowania i liczbie klastrów
for algorithm_name, Algorithm in clustering_algorithms.items():
    for n_clusters in n_clusters_list:
        # Inicjalizacja modelu
        algo = Algorithm(n_clusters=n_clusters, random_state=random_state)
        # Dopasowanie modelu do danych
        algo.fit(X)
        # Obliczenie metryk
        silhouette = metrics.silhouette_score(X, algo.labels_)
        davies_bouldin = metrics.davies_bouldin_score(X, algo.labels_)
        calinski_harabasz = metrics.calinski_harabasz_score(X, algo.labels_)
        # Dodanie wyników do tabeli
        results.append([algorithm_name, n_clusters, silhouette, davies_bouldin, calinski_harabasz])

# Konwersja wyników do tablicy NumPy
results = np.array(results)

# Wyświetlenie wyników w postaci tabeli
import pandas as pd
df = pd.DataFrame(results, columns=["Algorithm", "Number of Clusters", "Silhouette Score", "Davies-Bouldin Score", "Calinski-Harabasz Score"])
print(df)
# Zapisanie wyników do pliku tekstowego
df.to_csv('clustering_results.txt', index=False, sep='\t')

print("Wyniki zostały zapisane do pliku 'clustering_results.txt'.")
end_time = time.time()
execution_time = end_time - start_time
print("DBSCAN execution time:", execution_time, "seconds")

