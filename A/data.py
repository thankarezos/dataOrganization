import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import kmeans as km
import tree as tree
import os
import tkinter as tk
import dataframe as dfw
import tkWindow as tkw


pd.options.mode.chained_assignment = None 

script_path = os.path.abspath(__file__)
print(script_path)

data_file_path = os.path.join(os.path.dirname(script_path), 'data.csv')

df = pd.read_csv(data_file_path)


selected_columns = ['longmon', 'tollmon', 'equipmon', 'cardmon', 'wiremon', 'multline', 'voice', 'pager', 'internet', 'forward', 'confer', 'ebill']

data = df[selected_columns]

window = tkw.Window(500, 500, "Menu").window



def button1_clicked():
    km.elbow(data)

def button2_clicked():
    def submit():
        k = int(input_box.get())
        inputWindow.destroy()
        km.kmeans(data, k)
        
        
    inputWindow = tkw.Window(200, 100).window
    label = tk.Label(inputWindow, text="Enter cluster size")
    label.pack()
    input_box = tk.Entry(inputWindow)
    input_box.pack()

    # Create the submit button
    submit_button = tk.Button(inputWindow, text="Submit", command=submit)
    submit_button.pack()

    

def button3_clicked():
    tree.plot_dendrogram(data)

buttons = []

button = tk.Button(window, text="elbow", command=lambda: button1_clicked())
buttons.append(button)
button = tk.Button(window, text="kmeans", command=lambda: button2_clicked())
buttons.append(button)
button = tk.Button(window, text="dendrogram", command=lambda: button3_clicked())
buttons.append(button)

# Configure the buttons' width and height
for button in buttons:
    button.configure(width=20, height=4)

# Calculate the total number of buttons
num_buttons = len(buttons)

# Calculate the middle row index
middle_row = num_buttons // 2

# Position the buttons using the grid geometry manager
for i, button in enumerate(buttons):
    button.grid(row=i+1, column=1, pady=10)

# Add empty rows and columns to create space around the buttons
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(num_buttons+1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)
# Start the main event loop
window.mainloop()











# neighb = NearestNeighbors(n_neighbors=4) # creating an object of the NearestNeighbors class
# nbrs=neighb.fit(data) # fitting the data to the object
# distances,indices=nbrs.kneighbors(data) # finding the nearest neighbours

# # Sort and plot the distances results
# distances = np.sort(distances, axis = 0) # sorting the distances
# distances = distances[:, 1] # taking the second column of the sorted distances
# plt.plot(distances) # plotting the distances
# plt.show() # showing the plot

# # Perform DBSCAN clustering

# dbscan = DBSCAN(eps=16, min_samples=30)  # Adjust the parameters as per your data
# dbscan.fit(data)

# # data['cluster'] = dbscan.labels_

# print(data.head())

# pca = PCA(n_components=2)
# x = pca.fit_transform(data)

# x = pd.DataFrame(x)
# x['cluster'] = dbscan.labels_

# # plt.scatter(x[0], x[1], c=x['cluster'], labels=legend_labels)
# # plt.legend()
# sns.scatterplot(x=0, y=1, hue='cluster', data=x, palette='Set1')
# plt.show()