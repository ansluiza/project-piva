from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__, static_folder="static/")
app.config['SECRET_KEY'] = '619619'

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
        return render_template('logged.html')
    else:
        # false = user not found / senha incorreta
        print("user not found / senha incorreta")
        flash("E-mail ou senha incorretos!", "info")
        return redirect(url_for('login'))
    
    
    


if __name__ == '__main__':
    app.run(debug=True)