import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk
from DATABASE_MANAGER.database_manager import *

window = tk.Tk()
window.title('')
window.geometry('1800x640')

file_path = os.path.dirname(__file__)
db_path = os.path.dirname(__file__)
image_path = file_path+'/samsung.jpg'
caminho = 'cadastro.db'


#declara as variaveis de callback
global name_var
global pw_var
name_var = tk.StringVar()
pw_var = tk.IntVar()
pw_var.set(value=12345)
name_var.set(value='Miguel')

db_name = tk.StringVar()
db_age = tk.IntVar()
db_status = tk.StringVar()
db_hiring = tk.StringVar()
db_pw = tk.IntVar()
db_address = tk.StringVar()


db_age.set(value='')
db_name.set(value='')
db_status.set(value='')
db_hiring.set(value='')
db_pw.set(value='')
db_address.set(value='')



#cria frame para posicionar campos de login
bg_login_frame = tk.Frame(window, 
                          relief='flat',
                          width=1800, 
                          height=180, 
                          bg='navy')
bg_login_frame.pack(side='top')



#define campos para inserção de login
name_entry = tk.Entry(bg_login_frame, 
                      textvariable=name_var, 
                      width=50)
name_entry.place(x=930, y=30)

password_entry = tk.Entry(bg_login_frame, 
                          textvariable=pw_var, 
                          width=15 ,
                          show='*') 
password_entry.place(x=930, y=70)


#cria os labels de login; nome/email e senha
lbl_nome = tk.Label(bg_login_frame, 
                    text='Nome/email:', 
                    font='Times', 
                    bg='navy', 
                    cursor='arrow', 
                    fg='white')
lbl_nome.place(x=850, y=25)

lbl_senha = tk.Label(bg_login_frame, 
                     text='Senha:', 
                     font='Times', 
                     bg='navy', 
                     cursor='arrow',
                     fg='white')
lbl_senha.place(x=890, y=70)


#insere imagem de fundo
bg_image_bits = Image.open(image_path)

bg_image = ImageTk.PhotoImage(bg_image_bits)

lbl_bg_image = tk.Label(window, image=bg_image)
lbl_bg_image.place(x=0, y=180)


#cria janela com frames e labels para receberem os dados do perfil 
#do usuário
def profile_login():
    
    w_user = tk.Toplevel()
    w_user.geometry('960x720')
    bg_frame = tk.Frame(w_user, 
                        width=1320, 
                        height=320, 
                        relief='flat', 
                        bg='gray')
    bg_frame.place(x=20,y=0)

    user_picture_frame = tk.Frame(bg_frame, 
                                  width=160,
                                  height=180, 
                                  relief='flat', 
                                  bg='green')
    
    pic = Image.open(file_path+'/identidade.jpg')
    my_pic = ImageTk.PhotoImage(pic)
    lbl_pic = tk.Label(user_picture_frame, image=my_pic)
    lbl_pic.image = my_pic
    lbl_pic.pack(side='bottom')
   
    user_picture_frame.place(x=150, y=150)
    
    
    #insere os labels de identificação do perfil como nome, idade, endereço
    lbl_name = tk.Label(w_user, text='Nome:'+res[0][1], 
                        font='verdana',
                        bg='white',
                        fg='black')
    lbl_name.place(x=70,y=340)
    
    lbl_idade = tk.Label(w_user, 
                        text='Idade: '+res[0][3],
                        font='verdana',
                        bg='white',
                        fg='black')
    lbl_idade.place(x=70,y=390)
    
    lbl_endereco = tk.Label(w_user, text='Endereço: '+res[0][4],
                            font='verdana',
                            bg='white',
                            fg='black')
    lbl_endereco.place(x=70,y=430)
    
    lbl_status = tk.Label(w_user,text='STATUS: '+res[0][5],
                          bg='white',
                          fg='black')
    lbl_status.place(x=500,y=340)
    
    lbl_hiring = tk.Label(w_user,
                          text='CONTRATAÇÃO: '+res[0][6],
                          bg='white',
                          fg='black')
    lbl_hiring.place(x=600,y=340)
    

 
#valida nome e senha servindo como autenticação   
def validate():
    try:
        conn = sqlite3.connect('cadastro.db')
        c = conn.cursor()
        
        c.execute(sql_read_query, [(name_var.get(),pw_var.get())])
        global res
        res = c.fetchall()
        print(res[0][1])
    
    except Exception as tcv:
        print(f'Houve um erro: {tcv}')
    
    if [name_var.get(),pw_var.get()] == [res[0][1],res[0][2]]:
        profile_login()
        eraser_frame = tk.Frame(bg_login_frame, 
                                width=240,
                                height=20, 
                                bg='navy')
        eraser_frame.place(x=930,y=100)
        name_var.set(value='')
        pw_var.set(value='')
            
    elif [res[0][1],res[0][2]] != [name_var.get(),pw_var.get()]:
        alert_label = tk.Label(bg_login_frame, 
                               text='Usuário ou senha incorretos!', 
                               font='verdana', 
                               bg='navy', 
                               fg='red')
        alert_label.place(x=930, y=100)

#cria nova função para cadastrar novos funcionarios no banco de dados
def save_employee():
    try:
        name = db_name.get()
        password = db_pw.get()
        age = db_age.get()
        address = db_address.get()
        estatus = db_status.get()
        hiring = db_hiring.get()
        
        values = (name,password,age,address,estatus,hiring)

        vcon = db_conection(caminho)
        insert_data(vcon,sql_insert_query,values)
        if values != '':
            db_age.set(value='')
            db_name.set(value='')
            db_status.set(value='')
            db_hiring.set(value='')
            db_address.set(value='')
            db_pw.set(value='')
        lbl_alert = tk.Label(sign_win, 
                             text='Registro inserido com sucesso!')
        lbl_alert.place(x=50,y=400)
    except Exception as etc:
        print(etc)
    return True
        
    
        
#cria formulário para cadastro de novos funcionários
def profile_signin():
    global sign_win
    sign_win = tk.Toplevel()
    sign_win.geometry('640x420')
    
    lbl_entryName = tk.Label(sign_win, 
                             text='Nome:',
                             font='verdana',
                             bg='white',
                             fg='black')
    lbl_entryName.place(x=60,y=100)
    
    lbl_entryAge = tk.Label(sign_win, 
                             text='Idade:',
                             font='verdana',
                             bg='white',
                             fg='black')
    lbl_entryAge.place(x=60,y=150)
    
    lbl_entryStatus = tk.Label(sign_win, 
                             text='Status:',
                             font='verdana',
                             bg='white',
                             fg='black')
    lbl_entryStatus.place(x=60,y=200)
    
    lbl_entryHiring = tk.Label(sign_win, 
                             text='Contratação:',
                             font='verdana',
                             bg='white',
                             fg='black')
    lbl_entryHiring.place(x=10,y=250)
    
    lbl_entrypassword = tk.Label(sign_win, 
                             text='senha:',
                             font='verdana',
                             bg='white',
                             fg='black')
    lbl_entrypassword.place(x=10,y=350)
    
    lbl_entryaddress = tk.Label(sign_win, 
                             text='Endereço:',
                             font='verdana',
                             bg='white',
                             fg='black')
    lbl_entryaddress.place(x=10,y=400)
    
    sgn_entry_name = tk.Entry(sign_win,
                              textvariable=db_name, 
                              width=20,
                              bg='orange')
    sgn_entry_name.place(x=100,y=100)
    
    sgn_entry_age = tk.Entry(sign_win,
                             textvariable=db_age, 
                             width=20,
                             bg='orange')
    sgn_entry_age.place(x=100,y=150)
    
    sgn_entry_status = tk.Entry(sign_win,
                                textvariable=db_status,
                                width=20,
                                bg='orange')
    sgn_entry_status.place(x=100,y=200)
    
    sgn_entry_hiring = tk.Entry(sign_win,
                                textvariable=db_hiring,
                                width=20,
                                bg='orange')
    sgn_entry_hiring.place(x=100,y=250)
    
    sgn_entry_password = tk.Entry(sign_win,
                                textvariable=db_pw,
                                width=20,
                                bg='orange')
    sgn_entry_password.place(x=100,y=350)
    
    sgn_entry_address = tk.Entry(sign_win,
                                textvariable=db_address,
                                width=20,
                                bg='orange')
    sgn_entry_address.place(x=100,y=400)
    
    sgn_button = tk.Button(sign_win, 
                           text='Salvar',
                           bg='green',
                           fg='black',
                           command=save_employee)
    sgn_button.place(x=500,y=400)
    
    """value = save_employee()
    if value:
        lbl_alert = tk.Label(sign_win, 
                             text='Registro inserido com sucesso!')
        lbl_alert.place(x=50,y=400)
        
    elif not value:
        lbl_alert_error = tk.Label(sign_win, 
                             text='Houve um erro na inserção no registro!')
        lbl_alert_error.place(x=50,y=430)"""
        
        
    
    


#cria botões para cadastro e login
btn_cadastro = tk.Button(bg_login_frame, 
                         text='Cadastrar-se', 
                         command=profile_signin, 
                         bg='white', 
                         fg='black', 
                         width=10, 
                         height=1)
btn_cadastro.place(x=960, y=120)

btn_login = tk.Button(bg_login_frame, 
                      text='Login', 
                      command=validate, 
                      bg='white', 
                      fg='black', 
                      width=10, 
                      height=1)
btn_login.place(x=1270, y=25)



    




















window.mainloop()
