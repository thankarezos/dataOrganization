import pandas as pd
import numpy as np
import os
from tree import decision_tree
from knn import knn
from knn import models as knn_models
from tree import models as tree_models

script_path = os.path.abspath(__file__)

data_file_path = os.path.join(os.path.dirname(script_path), 'data.csv')

df = pd.read_csv(data_file_path)

columns_to_exclude = ['region', 'custcat']
data = df.drop(columns_to_exclude, axis=1)

print("===============================================")
while True:
    print("1. Decision Tree")
    print("2. KNN")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid choice")
        continue

    if choice == 1:
        while True:
            print(f"Chose numbers from 1 to {tree_models}") 
            try:
                option = int(input("Enter your choice: "))
            except:
                print("Invalid choice")
                continue

            if option in range(1, tree_models + 1):
                print("===============================================")
                decision_tree(data, option)
                break
            else:
                print("Invalid choice")
            
    elif choice == 2:
        while True:
            print(f"Chose numbers from 1 to {knn_models}") 
            try:
                option = int(input("Enter your choice: "))
            except:
                print("Invalid choice")
                continue

            if option in range(1, knn_models + 1):
                print("===============================================")
                knn(data, option)
                break
            else:
                print("Invalid choice")


            
    elif choice == 3:
        exit()
    else:
        print("Invalid choice")

# print(data.head())


