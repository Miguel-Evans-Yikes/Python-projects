import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk


file_path = os.path.dirname(__file__)


window = tk.Tk()
window.geometry('1024x683')
window.title('CONCESSIONÁRIA')

imagem = Image.open(file_path+'/concessionaria.jpg')

myimage = ImageTk.PhotoImage(imagem)

lbl_bg_image = tk.Label(window, image=myimage)
lbl_bg_image.place(x=330,y=0)

fm_main = tk.Frame(window, width=330, height=1024, relief='flat', bg='navy')
fm_main.place(x=0,y=0)

window.mainloop()












"""if __name__=='__main__':
    print(f'O diretório é: {file_path}')
"""









