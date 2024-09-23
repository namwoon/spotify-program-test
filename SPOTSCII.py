import tkinter as tk
from tkinter import ttk

#window object
window = tk.Tk()
window.title("SPOTSCII")
window.geometry('600x200')

#title
title_label = ttk.Label(master = window, text = "Welcome to SpotSCII!", font = "Roboto 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = "Search")
entry.pack()
button.pack()
input_frame.pack()

#run
window.mainloop()
