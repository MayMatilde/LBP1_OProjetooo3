from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from model.models import usuarios 


vamos_arrasar = Blueprint('vamos_arrasar', __name__)

#Página inicial🥳
@vamos_arrasar.route('/')
def visu():
    if 'name' in session:
        nome_usuario = session.get('name')
        return render_template('login.html', nome_usuario=nome_usuario)
    else:
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
                return redirect(url_for('vamos_arrasar.autentica'))
             else:
                 flash('Usuário ou senha inválidos!')
    return render_template('index.html')

#Rota autentica 😉
@vamos_arrasar.route('/autentica')
def autentica():
    return redirect(url_for('vamos_arrasar.login'))

#Rota logout😁
@vamos_arrasar.route('/logout')
def logout():
    session.pop('name', None) 
    return redirect(url_for('vamos_arrasar.login'))



