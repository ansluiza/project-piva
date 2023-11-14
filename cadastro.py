import sqlite3

# Configuração do banco de dados
DATABASE = 'banco_de_dados.db'


def cadastro_user(name, email, age, height, weight, sport_option, sport, gender):
    print("Executando Essa Função")
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO 'cadastro' VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (name, email, age, height, weight, sport_option, sport, gender))
        connection.commit()

    print("Terminou de Cadastrar No Banco De Dados")