from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from tkWindow import screen_center

def neighbors(data):
    neighb = NearestNeighbors(n_neighbors=4) # creating an object of the NearestNeighbors class
    nbrs=neighb.fit(data) # fitting the data to the object
    distances,indices=nbrs.kneighbors(data) # finding the nearest neighbours

    fig, ax = plt.subplots(figsize=(9, 6))
    # Sort and plot the distances results
    distances = np.sort(distances, axis = 0) # sorting the distances
    distances = distances[:, 1] # taking the second column of the sorted distances
    screen_center(fig)
    ax.plot(distances) # plotting the distances
    plt.show()

# Perform DBSCAN clustering

def dbscan(data, eps, min_samples):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples) # Adjust the parameters as per your data
    dbscan.fit(data)

    print(data.head())

    pca = PCA(n_components=2)
    x = pca.fit_transform(data)

    x = pd.DataFrame(x)
    x['cluster'] = dbscan.labels_

    fig, ax = plt.subplots(figsize=(9, 6))
    screen_center(fig)

    sns.scatterplot(x=0, y=1, hue='cluster', data=x, palette='Set1', ax=ax)
    plt.show()
