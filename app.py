from flask import Flask, render_template, request, redirect, flash, url_for
from cadastro import cadastro_user

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

if __name__ == '__main__':
    app.run(debug=True)