import sqlite3

# Configuração do banco de dados
DATABASE = 'banco_de_dados.db'


def cadastro_user(name, email, age, height, weight, sport_option, sport, gender):
    print("Executando Essa Função")
    insert_query = f"INSERT INTO cadastro VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)"
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(insert_query, (name, email, age, height, weight, sport_option, sport, gender))
        connection.commit()

    print("Terminou de Cadastrar No Banco De Dados")

def update_user(name, email, age, height, weight, sport_option, sport, gender, id):
    print("Executando Essa Função Update")
    update_query = f"UPDATE cadastro SET name = ?, email = ?, age = ?, height = ?, weight = ?, sport_option = ?, sport = ?, gender = ? WHERE id = ?"
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(update_query, (name, email, age, height, weight, sport_option, sport, gender, id))
        connection.commit()

    print("Terminou de Cadastrar No Banco De Dados")