import tkinter as tk
import tkWindow as tkw
import tksheet


def window (data):
    
    # column_widths = data.astype(str).apply(lambda x: x.str.len()).max()

    # text_widget_width = (sum(column_widths) + len(data.columns)) * 5
    # dataWindow = tkw.Window(text_widget_width * 8, 500, bg='darkblue').window
    print(data.head())
    dataWindow = tkw.Window(1200, 800, bg='darkblue').window

    sheet = tksheet.Sheet(dataWindow, data=data, width=1200, height=800)

    sheet.set_sheet_data(data.values.tolist())

    # Set the column names as the first row in the sheet
    sheet.headers(data.columns.tolist(), index="end")

    # Grid the Sheet widget
    sheet.grid(sticky="nsew")

    # dataWindow.geometry(f"{text_widget_width * 4}x500")
    # text_widget_height = 100  # Adjust the height as needed

    # text_widget = tk.Text(dataWindow, width=text_widget_width, height=text_widget_height)
    # text_widget.pack()

    # df_string = data.to_string(index=False)
    # text_widget.insert(tk.END, df_string)