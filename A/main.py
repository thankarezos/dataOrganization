import pandas as pd
import kmeans as km
import tree as tree
import os
import tkinter as tk
import tkWindow as tkw
import dbscan as dbs
from dataframe import window as dataframe

pd.options.mode.chained_assignment = None 

def main():
    script_path = os.path.abspath(__file__)

    data_file_path = os.path.join(os.path.dirname(script_path), 'data.csv')

    df = pd.read_csv(data_file_path)


    selected_columns = ['longmon', 'tollmon', 'equipmon', 'cardmon', 'wiremon', 'multline', 'voice', 'pager', 'internet', 'forward', 'confer', 'ebill']

    data = df[selected_columns]

    window = tkw.Window(500, 700, "Menu", bg='darkblue').window

    def button1_clicked():
        dataframe(data)

    def button2_clicked():
        km.elbow(data)

    def button3_clicked():
        def on_enter(event):
            submit()

        def submit():
            try:
                k = int(input_box.get())
                inputWindow.destroy()
                km.kmeans(data, k)
            except:
                print("error")
            
            
        inputWindow = tkw.Window(200, 100).window
        label = tk.Label(inputWindow, text="Enter cluster size")
        label.pack()
        input_box = tk.Entry(inputWindow)

        input_box.pack()

        input_box.bind("<Return>", on_enter)

        # Create the submit button
        submit_button = tk.Button(inputWindow, text="Submit", command=submit)
        submit_button.pack()

        

    def button4_clicked():
        tree.plot_dendrogram(data)

    def button5_clicked():
        dbs.neighbors(data)

    def button6_clicked():
        def on_enter(event):
            submit()

        def submit():
            try:
                eps = int(input_box.get())
                min_samples = int(input_box2.get())
                inputWindow.destroy()
                dbs.dbscan(data, eps, min_samples)
            except:
                print("error")
            inputWindow.destroy()
            dbs.dbscan(data, eps, min_samples)
            
            
        inputWindow = tkw.Window(200, 100).window
        label = tk.Label(inputWindow, text="Enter eps")
        label.pack()
        input_box = tk.Entry(inputWindow)
        input_box.insert(0, "16")
        input_box.pack()
        label = tk.Label(inputWindow, text="Enter min_samples")
        label.pack()
        input_box2 = tk.Entry(inputWindow)
        input_box2.insert(0, "30")
        input_box2.pack()

        input_box.bind("<Return>", on_enter)
        input_box2.bind("<Return>", on_enter)

        # Create the submit button
        submit_button = tk.Button(inputWindow, text="Submit", command=submit)
        submit_button.pack()

    buttons = []

    button = tk.Button(window, text="dataframe", command=lambda: button1_clicked())
    buttons.append(button)
    button = tk.Button(window, text="elbow", command=lambda: button2_clicked())
    buttons.append(button)
    button = tk.Button(window, text="kmeans", command=lambda: button3_clicked())
    buttons.append(button)
    button = tk.Button(window, text="dendrogram", command=lambda: button4_clicked())
    buttons.append(button)
    button = tk.Button(window, text="neighbour", command=lambda: button5_clicked())
    buttons.append(button)
    button = tk.Button(window, text="dbscan", command=lambda: button6_clicked())
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

if __name__ == "__main__":
    main()