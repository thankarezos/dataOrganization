import tkinter as tk


def window (data):
    dataWindow = tk.Tk()


    column_widths = data.astype(str).apply(lambda x: x.str.len()).max()


    text_widget_width = (sum(column_widths) + len(data.columns)) * 5
    print(text_widget_width)
    dataWindow.geometry(f"{text_widget_width * 4}x500")
    text_widget_height = 100  # Adjust the height as needed


    text_widget = tk.Text(dataWindow, width=text_widget_width, height=text_widget_height)
    text_widget.pack()


    df_string = data.to_string(index=False)
    text_widget.insert(tk.END, df_string)