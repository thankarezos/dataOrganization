import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import tkWindow as tkw

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