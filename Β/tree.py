import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

models = 4


def decision_tree(data, option=3):
    features = data.iloc[:, :-1]  # All columns except the last one
    labels = data.iloc[:, -1]  # Last column

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)


    if option == 1:
        clf = tree.DecisionTreeClassifier()
    elif option == 2:
        clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
    elif option == 3:
        clf = tree.DecisionTreeClassifier(criterion='gini', max_depth=3)
    elif option == 4:
        clf = tree.DecisionTreeClassifier(criterion='log_loss', max_depth=3)
        

    clf.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = clf.predict(X_test)

    print("Decision Tree:")

    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
