import sqlite3
import os




sql_ct = """CREATE TABLE colaboradores(ID INTEGER PRIMARY KEY AUTOINCREMENT
        NOT NULL,NOME VARCHAR(30) NOT NULL, FONE INTEGER NOT NULL);"""


def conectar():
    try:
        
        nome = input('Nome: ')
        telefone = int(input('Telefone: '))
        c = sqlite3.connect('cadastro.db')
        cn = c.cursor()
        sql = """INSERT INTO colaboradores(NOME, FONE) VALUES (nome,telefone);"""
        cn.execute(sql)
        print('dados inseridos com sucesso!')
    except Exception as e:
        print(f'erro devido a {e}')


if __name__=='__main__':
    conectar()

















