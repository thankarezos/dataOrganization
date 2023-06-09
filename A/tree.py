import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import tkWindow as tkw
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd

def plot_dendrogram(data):
    data = data.drop(['churn'], axis=1)
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
    churn = data['churn']
    data = data.drop(['churn'], axis=1)

    clustering = AgglomerativeClustering(n_clusters=k)
    clustering.fit(data)
    labels = clustering.labels_
    dataClustering = data.copy()
    dataClustering.loc[:, 'cluster'] = labels
    print(dataClustering)

    dataAgglo = data.copy()
    dataAgglo.loc[:, 'cluster'] = clustering.labels_
    dataAgglo.loc[:, 'Churned'] = churn
    churn_rate = dataAgglo.groupby('cluster')['Churned'].mean()
    problematic_cluster = churn_rate.idxmax()
    print('Problematic cluster: ', problematic_cluster)
    
    
    fig, ax = plt.subplots(figsize=(9,6))
    tkw.screen_center(fig)

    clustering = AgglomerativeClustering(n_clusters=k)
    x = PCA(n_components=2).fit_transform(data)
    clustering.fit(x)
    labels = clustering.labels_
    ax.scatter(x[:, 0], x[:, 1], c=labels)
    centroids = []
    for label in np.unique(labels):
        cluster_points = x[labels == label]
        centroid = np.mean(cluster_points, axis=0)
        centroids.append(centroid)
    
    pcadata = pd.DataFrame(x)
    pcadata.loc[:, 'cluster'] = clustering.labels_
    pcadata.loc[:, 'Churned'] = churn
    churn_rate = pcadata.groupby('cluster')['Churned'].mean()
    problematic_cluster = churn_rate.idxmax()
    print('Problematic cluster PCA: ', problematic_cluster)


    ax.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], marker='s', s=500, alpha=0.5)

    ax.set_title('Agglomerative Clustering')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Distance')
    plt.show()