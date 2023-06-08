import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.ensemble import IsolationForest

models = 8

def knn(data, option=8):

    features = data.iloc[:, :-1]  # All columns except the last one
    labels = data.iloc[:, -1]  # Last column

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)


   
    if option == 1:
        knn = KNeighborsClassifier(n_neighbors=9, metric='euclidean', n_jobs=-1, weights='distance', algorithm='brute')
    elif option == 2:
        knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean', n_jobs=-1, weights='distance', algorithm='brute')
    elif option == 3:
        knn = KNeighborsClassifier(n_neighbors=7, metric='euclidean', n_jobs=-1, weights='distance', algorithm='brute')
    elif option == 4:
        knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean', n_jobs=-1, weights='distance', algorithm='brute')
    elif option == 5:
        knn = KNeighborsClassifier(n_neighbors=7, metric='euclidean', n_jobs=-1, weights='distance', algorithm='auto', leaf_size=30)
    elif option == 6:
        knn = KNeighborsClassifier(n_neighbors=7, metric='minkowski', n_jobs=-1, weights='distance', algorithm='auto', leaf_size=30)
    elif option == 7:
        knn = KNeighborsClassifier(n_neighbors=7, metric='chebyshev', n_jobs=-1, weights='distance', algorithm='auto', leaf_size=30)
    elif option == 8:
        knn = KNeighborsClassifier(n_neighbors=7, metric='manhattan', n_jobs=-1, weights='distance', algorithm='brute', leaf_size=30)

    knn.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = knn.predict(X_test)

    print("KNN:")

    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')

    
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)