import sqlite3 # Biblioteca para interagir com bancos de dados SQLite nativamente no Python

def _executar(query):
    db_path = './contestLink' #Esse é o banco de dados
    connection = sqlite3.connect(db_path) #Conexão com o banco de dados (estamos criando a conexão)
    cursor = connection.cursor() #Tupla que armazena os dados do banco dedados (estamos criando o cursor)
    resultado = None

    try:
        cursor.execute(query)
        resultado = cursor.fetchall() #Organiza os dados da consulta
        connection.commit() #Persistencia da informação, para que a ação aconteça de forma efetiva

    except Exception as e: #Salva o erro como uma váriável para posterior exibição
        print(f'Erro na execução da query:\n{e}')
        
    finally:
        cursor.close() #Fecha o cursor
        connection.close() #Fecha a conexão
        return resultado