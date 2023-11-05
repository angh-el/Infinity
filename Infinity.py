
import tkinter as tk

original_window = tk.Tk()
original_window.title("Original Window")
original_window.geometry("400x300")

def on_closing():

    original_window.withdraw()

    # Create two new windows
    create_window()
    create_window()
    


def show_original_window():
    # Show the original window again
    original_window.deiconify()

def create_window():
    window = tk.Toplevel(original_window)
    window.title("New Window")
    window.geometry("400x300")
    window.protocol("WM_DELETE_WINDOW", on_closing)
    show_button = tk.Button(window, text="Show Original Window", command=show_original_window)
    show_button.pack()


original_window.protocol("WM_DELETE_WINDOW", on_closing)

original_window.mainloop()