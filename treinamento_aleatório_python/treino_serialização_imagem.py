import tkinter as tk
import os
from PIL import Image, ImageTk
from pickle import *

"""
-serializar uma imagem
-guardar os dados da imagem serializada no banco de dados
-reaver os dados de imagem serializados
-reconverter em imagem jpg
-exibir em uma janela

"""
tk.Tk().mainloop()

path = os.path.dirname(__file__)
PATH = path+'\empresa.jpg'


image = Image.open(PATH)

my_image = ImageTk.PhotoImage(image)

#image_cipher = loads(my_image)


print(my_image)

#window.mainloop()

