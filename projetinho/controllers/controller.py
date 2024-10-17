from flask import Blueprint, render_template, request, redirect, session, url_for
from model.models import User

Adm = User("Adm o melhor", "123adm")
Usuario1 = User ("UserCLT", "9090clt")
ListaUser = [Adm, Usuario1]

vamos_arrasar = Blueprint('arrasa', __name__)


@vamos_arrasar.route('/', methods=['POST', 'GET'])
def visu():
    user_acesso = session.get('user_acesso')
    return render_template('user.html', user=user_acesso)

@vamos_arrasar.before_app_request
def autentica_user():
    rota_segura = request.endpoint in ['arraso.protected']

    if rota_segura and 'user_acesso' not in session:
        print("Você precisa logar para acessar o sistema!")
        return redirect(url_for('arraso.index'))

@vamos_arrasar.route('/login', methods=['POST', 'GET'])
def Add():
    if request.method == 'POST':
       session['usuario'] = request.form['username']
       return redirect(url_for('arraso.index'))
    return render_template('index.html')


@vamos_arrasar.route('/autentica', methods=['POST'])
def autentica_user():
    username = request.form['username']
    password = request.form['password']
    
    for usuario in ListaUser:
        if usuario.validate(username, password):
            session['user_acesso'] = usuario.username
            print(f'{usuario.username} Só sucesso! Login feito')
            return redirect(url_for('arraso.index'))
    print('Usuário ou senha incorreta. 403')
    return redirect(url_for('arraso.login'))

@vamos_arrasar.route('/logout')
def logout():
    session.pop('user_acesso', None)
    return redirect(url_for('arraso.login'))
