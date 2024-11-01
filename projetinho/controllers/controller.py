from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from model.models import usuarios 


vamos_arrasar = Blueprint('vamos_arrasar', __name__)


#Página inicial🥳
@vamos_arrasar.route('/')
def visu():
    if 'name' in session:
        nome_usuario = session.get('name')
        return render_template('user.html', nome_usuario=nome_usuario)
    return render_template('user.html')
  

#Rota da página de login 😍
@vamos_arrasar.route('/login', methods=['GET', 'POST']) 
def login (): 
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        for usuario in usuarios:
            if nome == usuario.nome and senha == usuario.senha:
                session['name'] = usuario.nome
                return redirect(url_for('vamos_arrasar.autentica')) #renderiza a função autentica, porque deu certo
        flash('Usuário ou senha inválidos!', 'erro')
    return render_template('index.html')


#Rota autentica 😉
@vamos_arrasar.route('/autentica')
def autentica():
    return redirect(url_for('vamos_arrasar.visu'))

#Rota logout😁
@vamos_arrasar.route('/logout')
def logout():
    session.pop('name', None) 
    return redirect(url_for('vamos_arrasar.login'))


#request = pedido 
#  ____________Sessão_____________
# |                               |
# |          |--------|           |_______________________________
# |          |__name__|           |
# |                               |
# |_______________________________|


# Middleware: melhor é o *Before*
# Middleware melhor não criar no blueprint
#redirect.endpoint: não testa, o user pode acessar livremente 
#cookies sempre são guardados na requisão