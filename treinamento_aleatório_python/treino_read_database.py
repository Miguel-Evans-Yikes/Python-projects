import sqlite3

con = sqlite3.connect('cadastro.db')

conn = con.cursor()

myname = 'Miguel'
myage = 25
myaddress = 'my house'

#values=('junior',23,'rua da moca')
#try:
    #conn.execute('CREATE TABLE teste_data(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,nome VARCHAR(30) NOT NULL,idade INTEGER NOT NULL,endereço VARCHAR(30))')
    #print('tabela criada com sucesso!')
#except Exception as etc:
    
#   print(f'houve um erro: {etc}')

"""try:
    conn.execute('INSERT INTO teste_data(nome,idade,endereço) VALUES (?,?,?)',values)
    con.commit()
    print('dados inseridos com sucesso!')
except Exception as etc:
    print(f'Houve um erro: {etc}')
"""

try:
    user = "SELECT * FROM teste_data WHERE nome==?"
    c = conn.execute(user, [()])
    res = conn.fetchall()
    print(res[0][0])
    
except Exception as tcv:
    print(f'Houve um erro: {tcv}')


