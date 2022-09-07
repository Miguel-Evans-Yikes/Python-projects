import tkinter as tk


window = tk.Tk()
window.geometry('840x420')
window.title('Solucionador de Polinômio interpolador de Lagrange de 5 pontos. By Miguel Jr')

masterframe = tk.Frame(window, width=1200,height=700, bg='#2c5d63')
masterframe.place(x=0,y=0)

#declara as variáveis de callback
xk = tk.DoubleVar()
x0 = tk.DoubleVar()
x1 = tk.DoubleVar()
x2 = tk.DoubleVar()
x3 = tk.DoubleVar()
x4 = tk.DoubleVar()


xk.set(value='')
x0.set(value='')
x1.set(value='')
x2.set(value='')
x3.set(value='')
x4.set(value='')


#fk = tk.DoubleVar()
f0 = tk.DoubleVar()
f1 = tk.DoubleVar()
f2 = tk.DoubleVar()
f3 = tk.DoubleVar()
f4 = tk.DoubleVar()


#fk.set(value='')
f0.set(value='')
f1.set(value='')
f2.set(value='')
f3.set(value='')
f4.set(value='')
     




#declara os campos de entrada de X

entry_xk = tk.Entry(masterframe, textvariable=xk, width=40, bg='orange')
entry_xk.place(x=180, y=80)

entry_x0 = tk.Entry(masterframe, textvariable=x0,width=40, bg='orange')
entry_x0.place(x=180, y=130)

entry_x1 = tk.Entry(masterframe,textvariable=x1, width=40, bg='orange')
entry_x1.place(x=180, y=180)

entry_x2 = tk.Entry(masterframe,textvariable=x2, width=40, bg='orange')
entry_x2.place(x=180, y=230)

entry_x3 = tk.Entry(masterframe, textvariable=x3,width=40, bg='orange')
entry_x3.place(x=180, y=280)

entry_x4 = tk.Entry(masterframe, textvariable=x4,width=40, bg='orange')
entry_x4.place(x=180, y=330)



#declara os labels especificadores de variáveis de X
label_explain = tk.Label(masterframe, text='Valores de X', font=('verdana', 12))
label_explain.place(x=250, y=30)

label_xk = tk.Label(masterframe, text='XK', font=('verdana', 12))
label_xk.place(x=150, y=80)

label_x0 = tk.Label(masterframe, text='X0', font=('verdana', 12))
label_x0.place(x=150, y=130)

label_x1 = tk.Label(masterframe, text='X1', font=('verdana', 12))
label_x1.place(x=150, y=180)

label_x2 = tk.Label(masterframe, text='X2', font=('verdana', 12))
label_x2.place(x=150, y=230)

label_x3 = tk.Label(masterframe, text='X3', font=('verdana', 12))
label_x3.place(x=150, y=280)

label_x4 = tk.Label(masterframe, text='X4', font=('verdana', 12))
label_x4.place(x=150, y=330)




#declara os campos de entrada de f(x)

entry_f0 = tk.Entry(masterframe, textvariable=f0,width=40, bg='#a9d7f6')
entry_f0.place(x=530, y=130)

entry_f1 = tk.Entry(masterframe,textvariable=f1, width=40, bg='#a9d7f6')
entry_f1.place(x=530, y=180)

entry_f2 = tk.Entry(masterframe,textvariable=f2, width=40, bg='#a9d7f6')
entry_f2.place(x=530, y=230)

entry_f3 = tk.Entry(masterframe, textvariable=f3,width=40, bg='#a9d7f6')
entry_f3.place(x=530, y=280)

entry_f4 = tk.Entry(masterframe, textvariable=f4,width=40, bg='#a9d7f6')
entry_f4.place(x=530, y=330)



#declara os labels especificadores de variáveis de f(X)
label_explain1 = tk.Label(masterframe, text='Valores de f(x)', font=('verdana', 12))
label_explain1.place(x=580, y=30)


label_fk = tk.Label(masterframe, 
                    text='fK: Valor que se deseja encontrar', 
                    font=('verdana', 12))
label_fk.place(x=500, y=80)


label_f0 = tk.Label(masterframe, text='f0', font=('verdana', 12))
label_f0.place(x=500, y=130)

label_f1 = tk.Label(masterframe, text='f1', font=('verdana', 12))
label_f1.place(x=500, y=180)

label_f2 = tk.Label(masterframe, text='f2', font=('verdana', 12))
label_f2.place(x=500, y=230)

label_f3 = tk.Label(masterframe, text='f3', font=('verdana', 12))
label_f3.place(x=500, y=280)

label_f4 = tk.Label(masterframe, text='f4', font=('verdana', 12))
label_f4.place(x=500, y=330)
    

def calculate():
    

    try:        
        prod_dx = (xk.get()-x0.get())*(xk.get()-x1.get())*(xk.get()-x2.get())*(xk.get()-x3.get())*(xk.get()-x4.get())
            
        prod_lin_1 = (xk.get()-x0.get())*(x0.get()-x1.get())*(x0.get()-x2.get())*(x0.get()-x3.get())*(x0.get()-x4.get())

        prod_lin_2 = (x1.get()-x0.get())*(xk.get()-x1.get())*(x1.get()-x2.get())*(x1.get()-x3.get())*(x1.get()-x4.get())

        prod_lin_3 = (x2.get()-x0.get())*(x2.get()-x1.get())*(xk.get()-x2.get())*(x2.get()-x3.get())*(x2.get()-x4.get())

        prod_lin_4 = (x3.get()-x0.get())*(x3.get()-x1.get())*(x3.get()-x2.get())*(xk.get()-x3.get())*(x3.get()-x4.get())

        prod_lin_5 = (x4.get()-x0.get())*(x4.get()-x1.get())*(x4.get()-x2.get())*(x4.get()-x3.get())*(xk.get()-x4.get())

        somatorio = f0.get()/prod_lin_1+f1.get()/prod_lin_2+f2.get()/prod_lin_3+f3.get()/prod_lin_4+f4.get()/prod_lin_5

        fk = somatorio*prod_dx
    
        fk_short = '%.4f' % fk

        solution = f'Valor de fk: {fk_short}'

        frame_answer = tk.Frame(masterframe, width=350,height=50, bg='#2c5d63')
        frame_answer.place(x=150, y=440)

        lbl_answer = tk.Label(frame_answer, text=solution, font=('verdana', 12))
        lbl_answer.place(x=0, y=0)

        frame_cover_error = tk.Frame(masterframe, width=600, height=50,bg='#2c5d63')
        frame_cover_error.place(x=150,y=500)

    except (Exception,TypeError, tk.TclError):
        
        if tk.TclError:
            print('TclError')
            alert = 'Um ou mais dos valores fornecidos são inválidos!'
            lbl_error = tk.Label(masterframe, 
                            text=alert, 
                            font=('verdana', 12))
            lbl_error.place(x=150, y=500)

        elif ZeroDivisionError:
            print('divisão por zero')
            zero_alert = 'Houve uma tentativa de divisão por zero.Tente novamente!'
            lbl_zerodiv_error = tk.Label(masterframe, 
                            text=alert, 
                            font=('verdana', 12))
            lbl_zerodiv_error.place(x=150, y=550)



btn_calculate = tk.Button(window, text='Calcular', fg='green', 
                        bg='white', command=calculate)
btn_calculate.place(x=430, y=420)

def clear():
    xk.set(value='')
    x0.set(value='')
    x1.set(value='')
    x2.set(value='')
    x3.set(value='')
    x4.set(value='')

    f0.set(value='')
    f1.set(value='')
    f2.set(value='')
    f3.set(value='')
    f4.set(value='')

    frame_cover_error = tk.Frame(masterframe, width=600, height=50,bg='#2c5d63')
    frame_cover_error.place(x=150,y=500)

    frame_answer = tk.Frame(masterframe, width=350,height=50, bg='#2c5d63')
    frame_answer.place(x=150, y=440)
    

btn_clean = tk.Button(masterframe, text='limpar', fg='navy', command=clear)
btn_clean.place(x=630, y=380)    



def about():
    bio = tk.Toplevel()
    bio.geometry('640x420')
    bio.title('Sobre o autor')

    info = """Miguel E.L.Jr é estudante do curso de Engenharia da Computação da UNILAB.
    Tem python como sua linguagem de programação preferida e 
    gosta de tentar otimizar a resolução de problemas usando programação
    quando isso se mostra possível.

    Siga Miguel nas redes sociais:

    Instagram: @Miguel______jr
    Facebook: Miguel Júnior
    Twitch: Miguel_fallen_coder/dll
    """

    info_frame = tk.Frame(bio, width=1200, height=700, bg='#537895')
    info_frame.place(x=0,y=0)
    
    lbl_info = tk.Label(bio, text=info, font=('verdana', 12), bg='#537895', fg='white')
    lbl_info.place(x=30,y=30)


def help_me():
    bio = tk.Toplevel()
    bio.geometry('640x420')
    bio.title('Ajuda')

    instructions = """ - Este programa foi criado com o objetivo de solucionar problemas
    de interpolação polinomial envolvendo o polinômio interpolador de Lagrange
    que contenha até 5 pontos (x0,x1,x2,x3,x4) e xk que é o valor que será
    avaliado na função que se deseja descobrir seu fk. Esse caso se refere 
    ao polinômio interpolador de Lagrange para Interpolação direta. 

    -No caso da interpolação inversa xk tornar-se-à fk e os respectivos x deve-
    rão ser considerados f(x).

    -Para cada xk existe um f(xk) ou fk correspondente, conforme o caso, salvo
    exceções cujas não acontecem aqui.

    """
    
    help_frame = tk.Frame(bio, width=1200, height=700, bg='#09203f')
    help_frame.place(x=0,y=0)
    lbl_help = tk.Label(help_frame, 
                        text=instructions, 
                        font=('verdana', 12), 
                        bg='#09203f',
                        fg='white')
    lbl_help.place(x=10,y=20)


button = tk.Button(window, text='about', command=about)
button.place(x=600, y=500)

button_help = tk.Button(window, text='help', command=help_me)
button_help.place(x=10, y=500)




window.mainloop()


