from flask import Flask, app, render_template, request, redirect, flash, url_for
from cadastro import cadastro_user
import sqlite3

#criar uma funcao para saber se a tabela do banco ja existe(true ou false)
#criar uma funcao para criar a tabela do banco (OK)

def tabela_existente(banco_de_dados, cadastro):
    connection = sqlite3.connect(banco_de_dados)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name=cadastro")
    result = cursor.fetchone()
    return result is not None

    if tabela_existe(banco_de_dados, cadastro):
     print(f'A tabela {cadastro} existe no banco de dados {banco_de_dados}.')
    else:
     print(f'A tabela {cadastro} não existe no banco de dados {banco_de_dados}.')

    connection.close()


# Configuração do banco de dados
DATABASE = 'banco_de_dados.db'


def criar_tabela():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        # cursor.execute("""
        # CREATE TABLE cadastro (
        #         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        #         name TEXT NOT NULL,
        #         email TEXT NOT NULL,
        #         age INTEGER NOT NULL,
        #         height TEXT NOT NULL,
        #         weight TEXT NOT NULL,
        #         sport_option TEXT NOT NULL,
        #         sport TEXT NOT NULL,
        #         gender TEXT NOT NULL
        # );
        # """)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cadastro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name         TEXT NOT NULL,
                email        TEXT NOT NULL,
                age          INTERGER NOT NULL,
                height       FLOAT NOT NULL,
                weight       FLOAT NOT NULL,
                sport_option TEXT NOT NULL,
                sport        TEXT NOT NULL,
                gender       TEXT NOT NULL
            )
        ''')
        connection.commit()
criar_tabela()


def delete(id):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    # Construir a instrução DELETE
    delete = f"DELETE FROM cadastro WHERE id = ?"


    # Executar a instrução DELETE
    cursor.execute(delete, (id,))

    # Commit para aplicar as alterações
    conexao.commit()

    # Fechar a conexão com o banco de dados
    conexao.close()

def edit(id):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()
    
    # Construir a instrução UPDATE
    edit = f"edit cadastro SET id = ?"


    # Executar a instrução UPDATE
    cursor.execute(edit, (id,))

    # Commit para aplicar as alterações
    conexao.commit()

    # Fechar a conexão com o banco de dados
    conexao.close()

