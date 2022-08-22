import sqlite3
from sqlite3 import Error
import os

path = os.path.dirname(__file__)



    
sql_insert_query = """INSERT INTO users(NOME,SENHA,IDADE,ENDEREÇO,ESTATUS,CONTRATAÇÃO) VALUES (?,?,?,?,?,?)"""


sql_read_query = """SELECT * FROM users WHERE NOME==? AND SENHA==?"""


def sql_update_query():
    return """  """


def sql_delete_query():
    return """  """


#inicia a conexão com o banco de dados
def db_conection(_path):
    try:
        con = sqlite3.connect(_path)
    except Error as ex:
        print(ex)
    return con


#insere o registro no banco de dados recebe db_conection e 
# create_sql_query
def insert_data(conection,sql,values):
    try:
        c = conection.cursor()
        c.execute(sql,values)
        conection.commit()
        print('Novo registro inserido!')
        return True
    except Error as ex:
        print(ex)
        return False


def read():
    pass


def update():
    pass


def delete():
    pass





