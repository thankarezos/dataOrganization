import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from tkWindow import screen_center
import os



def elbow(data):
    data = data.drop(['churn'], axis=1)
    sse = []
    for i in range(1,11):
        kmeans = KMeans(n_clusters=i, n_init='auto')
        kmeans.fit(data)
        sse.append(kmeans.inertia_)

    fig, ax = plt.subplots(figsize=(9,6))
    
    screen_center(fig)

    ax.plot(range(1,11), sse, marker='o')
    ax.set_title('Elbow curve')
    ax.set_xlabel('Number of clusters')
    ax.set_ylabel('SSE')




    plt.show()

def kmeans(data, k):
    churn = data['churn']
    data = data.drop(['churn'], axis=1)
    
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=1).fit(data)
    # data.loc[:, 'cluster'] = kmeans.labels_
    dataKmeans = data.copy()
    dataKmeans.loc[:, 'cluster'] = kmeans.labels_
    print("=====================================")
    print("Kmeans")
    print(dataKmeans)
    dataKmeans.loc[:, 'Churned'] = churn

    # print(dataKmeans)
    churn_rate = dataKmeans.groupby('cluster')['Churned'].mean()
    problematic_cluster = churn_rate.idxmax()
    
    print('Problematic cluster: ', problematic_cluster)

    pca = PCA(n_components=2)
    x = pca.fit_transform(data)
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=1)
    kmeans.fit(x)
    pcadata = pd.DataFrame(x)
    pcadata.loc[:, 'cluster'] = kmeans.labels_
    pcadata.loc[:, 'Churned'] = churn
    churn_rate = pcadata.groupby('cluster')['Churned'].mean()
    problematic_cluster = churn_rate.idxmax()
    print('Problematic cluster PCA: ', problematic_cluster)

    fig, ax = plt.subplots(figsize=(9,6))

    screen_center(fig)

    ax.scatter(x[:, 0], x[:, 1], c=kmeans.labels_)
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1] , marker='s', s=500, alpha=0.5)
    plt.show()