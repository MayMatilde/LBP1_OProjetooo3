from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from model.models import User

Adm = User("Adm o melhor", "123adm")
Usuario1 = User ("UserCLT", "9090clt")
ListaUser = [Adm, Usuario1]

vamos_arrasar = Blueprint('arraso', __name__)

#Página inicial!!! =)🥳
@vamos_arrasar.route('/', methods=['POST', 'GET'])
def visu():
    user_acesso = session.get('user_acesso')
    return render_template('user.html', user=user_acesso)

# @vamos_arrasar.before_request
# def autentica_user():
#     segura = request.endpoint in ['arraso.protected']

#     if segura and 'user_acesso' not in session:
#         flash("Você precisa logar para acessar o sistema!")
#         return redirect(url_for('arraso.index'))


#rota do login =)🥰 and self.password == passwo and self.password == passwordrd
@vamos_arrasar.route('/login', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
       session['usuario'] = request.form['username']
       return redirect(url_for('arraso.index'))
    return render_template('index.html')

#rota autentica=)😀
@vamos_arrasar.route('/autentica', methods=['POST'])
def autentica_user():
    username = request.form['username']
    password = request.form['password']
    
    for User in ListaUser:
        if username == User.usernameCLT and password == User.password:
            session['user_acesso'] = User.usernameCLT
            flash(f'{User.usernameCLT} Só sucesso! Login feito')
            return redirect(url_for('arraso.index'))
    flash('Usuário ou senha incorreta. 403')
    return redirect(url_for('arraso.html'))

#rota logout =)😍
@vamos_arrasar.route('/logout')
def logout():
    session.pop('user_acesso', None)
    return redirect(url_for('arraso.login'))
