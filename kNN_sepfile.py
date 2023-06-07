import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

train_filename = 'Datasets/iris-train.csv'
test_filename = 'Datasets/iris-test.csv'

data = pd.read_csv(train_filename)
class_train = data.iloc[:, -1]
attr_train = data.iloc[:, 0:-1]

data = pd.read_csv(test_filename)
class_test = data.iloc[:, -1]
attr_test = data.iloc[:, 0:-1]


model = KNeighborsClassifier(n_neighbors=1, algorithm='kd_tree',leaf_size=5,metric='euclidean')
model.fit(attr_train, class_train)

predictions = model.predict(attr_test)

print(metrics.accuracy_score(class_test, predictions))
precision, recall, fscore, supp = metrics.precision_recall_fscore_support(class_test, predictions,average=None)
print(precision)
print(recall)
print(fscore)

confusion_matrix = metrics.confusion_matrix(class_test, predictions)
#print(c_m)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
cm_display.plot()
plt.show()
