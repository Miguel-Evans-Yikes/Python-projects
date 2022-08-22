
from tkinter import ttk,tix
import tkinter as tk 
import os
from PIL import Image, ImageTk

path = os.path.dirname(__file__)

window = tk.Tk()
def fileopen():
    file = tk.tix.filedialog.LoadFileDialog(window)
    

    print(file)
btn = tk.Button(window, text='open file',command=fileopen)
btn.place(x=150, y=150)











window.mainloop()



