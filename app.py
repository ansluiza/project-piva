from flask import Flask, render_template, request, redirect, flash, url_for
from cadastro import cadastro_user, update_user
import sqlite3
from criar_banco import delete

app = Flask(__name__, static_folder="static/")
app.config['SECRET_KEY'] = '619619'

DATABASE_PATH = 'banco_de_dados.db'

@app.route('/') # uma rota que renderiza a página
@app.route('/login')
def login(): # com uma função para renderizar a página
    return render_template('index.html')

@app.route('/login_handler', methods=['POST']) # uma rota similar que cuida dos eventos ocorridos daquela página
def login_handle(): # ela vai cuidar da verificação de login
    # verificar username
    # verificar a senha
    db_user = "Ana"
    db_password = "123456"
    username = request.form['username-input']
    password = request.form['password-input']

    print(f"Username:{username}")
    print(f"Password:{password}")

    # saidas
    if username.lower() == db_user.lower() and password == db_password:
        # true = user logado
        print("Logado")
        return render_template('register.html')
    else:
        # false = user not found / senha incorreta
        print("user not found / senha incorreta")
        flash("Username ou senha incorretos!", "info")
        return redirect(url_for('login'))

@app.route('/register')
def register():
    return render_template('register.html')
    
@app.route('/register_handler', methods=['POST']) # uma rota similar que cuida dos eventos ocorridos daquela página
def register_handle(): # ela vai cuidar da verificação de login
    request_json = request.form

    print(request_json)

    name = request.form['name-input']
    email = request.form['e-mail-input']
    age = request.form['number-input']
    height = request.form['height-input']
    weight = request.form['weight-input']
    gender = request.form['gender']
    sport_option = request.form['sport-option']
    sport = request.form['sport']

    print(f"name:{name}")
    print(f"email:{email}")
    print(f"number:{age}")
    print(f"height:{height}")
    print(f"weight:{weight}")

    # Conexão com o banco
    # banco = sqlite3.connect(DATABASE_PATH)
    # cursor = banco.cursor()

    # insert_query = "INSERT INTO CUSTOMERS "
    cadastro_user(name, email, age, height, weight, sport_option, sport, gender)

    return redirect(url_for('register'))



@app.route('/data')
def data():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cadastro')
    dados = cursor.fetchall()
    connection.close()

    print("Dados Banco:", dados)
    return render_template('data.html', dados=dados)

@app.route('/data/deleteStudent')
def deleteStudent():
    student_id = request.args.get('student')

    print("Student ID:", student_id)
    delete(student_id)
    return redirect(url_for('data'))
    
@app.route('/edit_handler', methods=['POST']) # uma rota similar que cuida dos eventos ocorridos daquela página
def edit_handle(): # ela vai cuidar da verificação de login
    request_json = request.form
    student_id = request.args.get('student')
    print(request_json)

    name = request.form['name-input']
    email = request.form['e-mail-input']
    age = request.form['number-input']
    height = request.form['height-input']
    weight = request.form['weight-input']
    gender = request.form['gender']
    sport_option = request.form['sport-option']
    sport = request.form['sport']

    print(f"name:{name}")
    print(f"email:{email}")
    print(f"number:{age}")
    print(f"height:{height}")
    print(f"weight:{weight}")

    # Conexão com o banco
    # banco = sqlite3.connect(DATABASE_PATH)
    # cursor = banco.cursor()

    # insert_query = "INSERT INTO CUSTOMERS "
    update_user(name, email, age, height, weight, sport_option, sport, gender, student_id)
    return redirect(url_for('data'))

@app.route('/data/editStudent')
def editStudent():
    student_id = request.args.get('student')

    print("Student ID:", student_id)
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cadastro WHERE id = ?', (student_id,))
    dados = cursor.fetchone()
    connection.close()
    print(dados)
    return render_template('edit.html', dados=dados, student=student_id)

    
@app.route('/data_handler', methods=['POST']) # uma rota similar que cuida dos eventos ocorridos daquela página
def data_handle(): # ela vai cuidar da verificação de login
    request_json = request.form

    print(request_json)


if __name__ == '__main__':
    app.run(debug=True)