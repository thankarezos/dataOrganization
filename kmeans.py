#https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

iris = pd.read_csv('iris.csv')

print(iris.head())
print(iris.info())

sns.scatterplot(x='a', y='c',  hue='class', data=iris, color='blue')
plt.savefig('scatterplot1.png')
plt.show();
sns.scatterplot(x='a', y='b',  hue='class', data=iris, color='blue')
plt.savefig('scatterplot2.png')
plt.show();
sns.scatterplot(x='a', y='d',  hue='class', data=iris, color='blue')
plt.savefig('scatterplot3.png')
plt.show();
sns.scatterplot(x='b', y='c',  hue='class', data=iris, color='blue')
plt.savefig('scatterplot4.png')
plt.show();
sns.scatterplot(x='b', y='d',  hue='class', data=iris, color='blue')
plt.savefig('scatterplot5.png')
plt.show();
sns.scatterplot(x='c', y='d',  hue='class', data=iris, color='blue')
plt.savefig('scatterplot6.png')
plt.show();

data = iris.iloc[:, 0:-1] # clustering based on 4 columns

#elbow method
sse = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, n_init='auto')
    kmeans.fit(data)
    sse.append(kmeans.inertia_)

plt.plot(range(1,11), sse, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('inertia/SSE')
plt.show()

kmeans = KMeans(n_clusters=3, n_init='auto')
kmeans.fit(data)

print('SSE:',kmeans.inertia_)
print('Final locations of the centroid:',kmeans.cluster_centers_)
print("The number of iterations required to converge", kmeans.n_iter_)

#print(kmeans.labels_)

iris['cluster'] = kmeans.labels_.tolist()

sns.scatterplot(x='a', y='c',  hue='cluster', data=iris, color='blue')
plt.savefig('scatterplot7.png')
plt.show();
sns.scatterplot(x='a', y='b',  hue='cluster', data=iris, color='blue')
plt.savefig('scatterplot8.png')
plt.show();
sns.scatterplot(x='a', y='d',  hue='cluster', data=iris, color='blue')
plt.savefig('scatterplot9.png')
plt.show();
sns.scatterplot(x='b', y='c',  hue='cluster', data=iris, color='blue')
plt.savefig('scatterplot10.png')
plt.show();
sns.scatterplot(x='b', y='d',  hue='cluster', data=iris, color='blue')
plt.savefig('scatterplot11.png')
plt.show();
sns.scatterplot(x='c', y='d',  hue='cluster', data=iris, color='blue')
plt.savefig('scatterplot12.png')
plt.show();

print(iris)
iris.to_csv('iris_clusterAssignments.csv')

df2 = pd.DataFrame(iris ,columns = ["a","b","c","d"])
df2['Clusters']=kmeans.labels_
print(df2)
parallel_coordinates(df2, 'Clusters',color=('#383c4a','#0a3661','#dcb536'))
plt.show()

