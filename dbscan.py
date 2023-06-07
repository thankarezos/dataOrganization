#https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html

from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

iris = pd.read_csv('Datasets/iris.csv')

data = iris.iloc[:, 0:-1] # clustering based on 4 columns


#search for the eps parameter value
from sklearn.neighbors import NearestNeighbors # importing the library
neighb = NearestNeighbors(n_neighbors=2) # creating an object of the NearestNeighbors class
nbrs=neighb.fit(data) # fitting the data to the object
distances,indices=nbrs.kneighbors(data) # finding the nearest neighbours

# Sort and plot the distances results
distances = np.sort(distances, axis = 0) # sorting the distances
distances = distances[:, 1] # taking the second column of the sorted distances
plt.plot(distances) # plotting the distances
plt.show() # showing the plot

neighb = NearestNeighbors(n_neighbors=4) # creating an object of the NearestNeighbors class
nbrs=neighb.fit(data) # fitting the data to the object
distances,indices=nbrs.kneighbors(data) # finding the nearest neighbours

# Sort and plot the distances results
distances = np.sort(distances, axis = 0) # sorting the distances
distances = distances[:, 1] # taking the second column of the sorted distances
plt.plot(distances) # plotting the distances
plt.show() # showing the plot

#parameter eps=0.4
dbscan = DBSCAN(eps = 0.4, min_samples = 4)
dbscan.fit(data)

iris['cluster'] = dbscan.labels_.tolist()

sns.scatterplot(x='a', y='c',  hue='cluster', data=iris, color='blue')
plt.savefig('scatterplot.png')
plt.show();

print(iris)
iris.to_csv('iris_clusterAssignmentsDBScan.csv')

df2 = pd.DataFrame(iris ,columns = ["a","b","c","d"])
df2['Clusters']=dbscan.labels_
print(df2)
parallel_coordinates(df2, 'Clusters',color=('red','blue','green', "yellow", "black"))
plt.show()
