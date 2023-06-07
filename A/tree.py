import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

def plot_dendrogram(data):
    Z = linkage(data, method='ward')
    fig, ax = plt.subplots(figsize=(9,6))
    # Plot the dendrogram
    dendrogram(Z, ax=ax)
    ax.set_title('Agglomerative Clustering - Dendrogram')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Distance')
    plt.show()