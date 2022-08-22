import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk


#cria janela principal de alto nível
window = tk.Tk()
window.geometry('1024x960')
window.title('')


#define as variáveis de recursão
file_path = os.path.dirname(__file__)

global var_name
var_name = tk.StringVar()

global var_age
var_age = tk.IntVar()
var_age.set(value='')

global var_fcolor
var_fcolor = tk.StringVar()


#insere o frame de cor azul marinho
fm_main = tk.Frame(window, width=300, height=960, relief='flat', bg='navy')
fm_main.place(x=0, y=0)


#insere imagem de fundo
image = Image.open(file_path+'/landscape.jpg')
bg_image = ImageTk.PhotoImage(image)
lbl_bg_image = tk.Label(window, image=bg_image)
lbl_bg_image.place(x=300,y=0)


#insere os labels de nome, idade e cor favorita
lbl_name = tk.Label(fm_main, text='Name:', font='Verdana', bg='yellow')
lbl_name.place(x=100, y=80)

lbl_age = tk.Label(fm_main, text='Age:', font='Verdana', bg='yellow')
lbl_age.place(x=100, y=160)

lbl_f_color = tk.Label(fm_main, text='Favorite color', font='Verdana', bg='yellow')
lbl_f_color.place(x=100, y=240)


#insere as entradas para nome, idade e cor favorita
ent_f_color = tk.Entry(fm_main, textvariable=var_fcolor, width=25, bg='orange')

ent_f_color.place(x=100, y=270)

ent_name = tk.Entry(fm_main, textvariable=var_name, width=20, bg='orange')
ent_name.place(x=100,y=115)

ent_age = tk.Entry(fm_main, textvariable=var_age, width=20, bg='orange')
ent_age.place(x=100, y=195)


#função para inserir os dados no label pop-up
def insertData():
    age = var_age.get()
    name = var_name.get()
    fcolor = var_fcolor.get()
    
    fm_response = tk.Frame(fm_main, relief='flat', width=250, height=180, bg='grey')
    
    lbl_nameVar = tk.Label(fm_response, text=f'Name: {name}', font='Verdana', bg='red')
    lbl_nameVar.place(x=50,y=50)
    
    lbl_ageVar = tk.Label(fm_response, text=f'Age: {age}', font='Verdana', bg='green')
    lbl_ageVar.place(x=50, y=85)

    lbl_fcolor = tk.Label(fm_response, text=f'Favorite color: {fcolor}', font='Verdana', bg='yellow')
    lbl_fcolor.place(x=50, y=120)
    
    fm_response.place(x=50, y=350)
    var_name.set(value='')
    var_age.set(value='')
    var_fcolor.set(value='')
    window.update()

def cleanData():
    fm_clean = tk.Frame(fm_main, relief='flat', width=250, height=180, bg='navy')
    fm_clean.place(x=50, y=350)


#botão para inserir os dados na treeview
btn_insert = tk.Button(fm_main, text='Enviar', font='Verdana', bg='green',width=10, command=insertData)
btn_insert.place(x=120, y=600)

btn_clean = tk.Button(fm_main, text='Limpar', font='Verdana', bg='white', width=10, command=cleanData)
btn_clean.place(x=120, y=640)


#insere os dados no treeview

















window.mainloop()
