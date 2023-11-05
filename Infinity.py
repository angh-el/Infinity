# import tkinter as tk

# def on_closing(window):
#     # Hide the original window
#     window.withdraw()

#     # Create two new windows
#     # new_window1 = tk.Toplevel(window)
#     # new_window1.title("New Window 1")
#     # new_window2 = tk.Toplevel(window)
#     # new_window2.title("New Window 2")

#     create_window()
#     create_window()
    
#     # Add widgets or perform any actions in the new windows

# def show_original_window():
#     # Show the original window again
#     window.deiconify()




# def create_window():
#     window = tk.Tk()
#     window.title("My Window")
#     window.geometry("400x300")
#     window.protocol("WM_DELETE_WINDOW", on_closing)
#     # window.protocol("WM_DELETE_WINDOW", on_closing)
#     show_button = tk.Button(window, text="Show Original Window", command=show_original_window)
#     show_button.pack()
#     window.mainloop()

# # Set the window title

# create_window()

import tkinter as tk

original_window = tk.Tk()
original_window.title("Original Window")
original_window.geometry("400x300")

def on_closing():
    # Hide the original window
    original_window.withdraw()

    # Create two new windows
    create_window()
    create_window()
    
    # Add widgets or perform any actions in the new windows

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

# Configure the original window to call the on_closing function when closed
original_window.protocol("WM_DELETE_WINDOW", on_closing)

original_window.mainloop()