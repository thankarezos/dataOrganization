import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import tkinter as tk
import tkWindow as tkw
import matplotlib  
# matplotlib.use("TkAgg")

def elbow(data):
    sse = []
    for i in range(1,11):
        kmeans = KMeans(n_clusters=i, n_init='auto')
        kmeans.fit(data)
        sse.append(kmeans.inertia_)

    fig, ax = plt.subplots(figsize=(9,6))
    
    tkw.screen_center(fig)

    ax.plot(range(1,11), sse, marker='o')
    ax.set_title('Elbow curve')
    ax.set_xlabel('Number of clusters')
    ax.set_ylabel('SSE')




    plt.show()

def kmeans(data, k):

    kmeans = KMeans(n_clusters=k, random_state=0, n_init=1).fit(data)
    # data.loc[:, 'cluster'] = kmeans.labels_
    print(data.head())

    pca = PCA(n_components=2)
    x = pca.fit_transform(data)
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=1)
    kmeans.fit(x)

    fig, ax = plt.subplots(figsize=(9,6))

    ax.scatter(x[:, 0], x[:, 1], c=kmeans.labels_)
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1] , marker='s', s=500, alpha=0.5)
    plt.show()