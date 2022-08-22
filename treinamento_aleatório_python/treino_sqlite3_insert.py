import sqlite3
import tkinter as tk


window = tk.Tk()
window.geometry('960x720')
window.title('')
name_var = tk.StringVar()
phone_var = tk.IntVar()
phone_var.set(value='')


name_entry = tk.Entry(window, 
                      textvariable=name_var, 
                      width=30, bg='orange').place(x=100,y=150)

phone_entry = tk.Entry(window, 
                       textvariable=phone_var, 
                       width=15, bg='orange').place(x=100, y=200)

tk.Label(window, text='Nome:', bg='grey',fg='black').place(x=55,y=150)

tk.Label(window, text='Telefone:',bg='grey', fg='black').place(x=40,y=200)



def save_data():
    try:
        nome = name_var.get()
        fone = phone_var.get()
        c = sqlite3.connect('database.db')
        conn = c.cursor()
        values = (nome, fone)
    
        conn.execute('INSERT INTO registros(NOME,FONE) VALUES (?,?)', values)
        c.commit()
        lbl_alert = tk.Label(window,text='registro inserido com sucesso!')
        lbl_alert.place(x=300,y=600)
    #conn.execute("""CREATE TABLE registros(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                #NOME VARCHAR(30) NOT NULL,FONE INTEGER NOT NULL)""")"""
    #print('tabela criada!')
    
    except Exception as etc:
        print(etc)
    
    


btn = tk.Button(window, text='Salvar', command=save_data, bg='green')
btn.place(x=400, y=500)







window.mainloop()