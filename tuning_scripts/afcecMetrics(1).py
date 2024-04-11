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

data_1 = np.loadtxt('c12_data.txt', delimiter='\t')
data_2 = np.loadtxt('c12_noise_data.txt', delimiter='\t')
data_3 = np.loadtxt('3N_forces_data.txt', delimiter='\t')
data_4 = np.loadtxt('3N_forces_noise_data.txt', delimiter='\t')

labels_1 = np.loadtxt('labels1.txt', delimiter='\t')
labels_2 = np.loadtxt('labels2.txt', delimiter='\t')
labels_3 = np.loadtxt('labels_3.txt', delimiter='\t')
labels_4 = np.loadtxt('labels_4.txt', delimiter='\t')

cluster_labels3 = labels_3
# Obliczanie Silhouette Score
silhouette_score3 = metrics.silhouette_score(data_3, cluster_labels3)
# Obliczanie Davies-Bouldin Index
db_index3 = metrics.davies_bouldin_score(data_3, cluster_labels3)
# Obliczanie Calinski-Harabasz Index
ch_index3 = metrics.calinski_harabasz_score(data_3, cluster_labels3)

print("Silhouette Score:", silhouette_score3)
print("Davies-Bouldin Index:", db_index3)
print("Calinski-Harabasz Index:", ch_index3)

cluster_labels4 = labels_4
# Obliczanie Silhouette Score
silhouette_score4 = metrics.silhouette_score(data_4, cluster_labels4)
# Obliczanie Davies-Bouldin Index
db_index4= metrics.davies_bouldin_score(data_4, cluster_labels4)
# Obliczanie Calinski-Harabasz Index
ch_index4 = metrics.calinski_harabasz_score(data_4, cluster_labels4)

print("Silhouette Score:", silhouette_score4)
print("Davies-Bouldin Index:", db_index4)
print("Calinski-Harabasz Index:", ch_index4)

end_time = time.time()
# Pomiar czasu wykonania
execution_time = end_time - start_time
print("DBSCAN execution time:", execution_time, "seconds")
      
with open('afcec_metrics_results.txt', 'w') as f:
    # Zapisanie wyników do pliku
    f.write("Silhouette Score4: {}\n".format(silhouette_score4))
    f.write("Davies-Bouldin Index4: {}\n".format(db_index4))
    f.write("Calinski-Harabasz Index4 {}\n".format(ch_index4))
    f.write("Silhouette Score3: {}\n".format(silhouette_score3))
    f.write("Davies-Bouldin Index3: {}\n".format(db_index3))
    f.write("Calinski-Harabasz Index3 {}\n".format(ch_index3))

    f.write("DBSCAN execution time: {} seconds\n".format(execution_time))

