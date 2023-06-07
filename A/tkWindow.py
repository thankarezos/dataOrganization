

import tkinter

class Window:
    def __init__(self, window_width, window_height, window_title=""):
        self.window = tkinter.Tk()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.window.title(window_title)

def screen_center(fig):
    # Create a dummy canvas to access the Tk window
    window = tkinter.Tk()

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Get the figure width and height
    fig_width, fig_height = fig.get_size_inches()

    # Calculate the position to center the figure
    x = (screen_width - fig_width * window.winfo_fpixels('1i')) // 2
    y = (screen_height - fig_height * window.winfo_fpixels('1i')) // 2

    # Set the figure's position using wm_geometry
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))

    # Destroy the Tkinter window
    window.destroy()