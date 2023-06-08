import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import tkWindow as tkw
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
import numpy as np

def plot_dendrogram(data):
    Z = linkage(data, method='ward')
    fig, ax = plt.subplots(figsize=(9,6))
    tkw.screen_center(fig)
    # Plot the dendrogram
    dendrogram(Z, ax=ax, truncate_mode='lastp', p=40, leaf_rotation=45., leaf_font_size=10., show_contracted=True,)
    ax.set_title('Agglomerative Clustering - Dendrogram')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Distance')
    plt.show()

def agglomerativeClustering(data, k):
    clustering = AgglomerativeClustering(n_clusters=k)
    clustering.fit(data)
    labels = clustering.labels_
    dataClustering = data.copy()
    dataClustering.loc[:, 'cluster'] = labels
    print(dataClustering)
    fig, ax = plt.subplots(figsize=(9,6))
    tkw.screen_center(fig)

    x = PCA(n_components=2).fit_transform(data)
    clustering.fit(x)
    labels = clustering.labels_
    ax.scatter(x[:, 0], x[:, 1], c=labels)
    centroids = []
    for label in np.unique(labels):
        cluster_points = x[labels == label]
        centroid = np.mean(cluster_points, axis=0)
        centroids.append(centroid)

    ax.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], marker='s', s=500, alpha=0.5)

    ax.set_title('Agglomerative Clustering')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Distance')
    plt.show()