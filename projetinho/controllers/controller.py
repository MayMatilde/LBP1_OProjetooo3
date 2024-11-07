from flask import Blueprint, render_template, request, redirect, session, url_for, flash, make_response
from model.models import usuarios, versiculos_por_topico 

vamos_arrasar = Blueprint('vamos_arrasar', __name__)

# Página inicial🥳
@vamos_arrasar.route('/')
def visu():
    if 'name' in session:
        nome_usuario = session.get('name')
        topicos = versiculos_por_topico.keys()
        return render_template('user.html', nome_usuario=nome_usuario, topicos=topicos)
    return render_template('user.html', topicos=[])

# Rota da página de login 😍
@vamos_arrasar.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        for usuario in usuarios:
            if nome == usuario.nome and senha == usuario.senha:
                session['name'] = usuario.nome
                return redirect(url_for('vamos_arrasar.autentica')) 
        flash('Usuário ou senha inválidos!', 'erro')
    return render_template('index.html')

# Rota autentica 😉
@vamos_arrasar.route('/autentica')
def autentica():
    topico_selecionado = request.cookies.get('topico_selecionado')
    versiculo = versiculos_por_topico.get(topico_selecionado, "Selecione um tópico")
    return render_template('versiculo.html', topico=topico_selecionado, versiculo=versiculo)

@vamos_arrasar.route('/selecionar_topico', methods=['POST'])
def selecionar_topico():
    if request.method == 'POST':
        topico = request.form.get('topico')
        if topico not in versiculos_por_topico:
            return 'Tópico inválido'
        resposta = make_response(redirect(url_for('vamos_arrasar.autentica')))
        resposta.set_cookie('topico_selecionado', topico, max_age=60 * 60 * 24)
        return resposta

# Rota logout😁
@vamos_arrasar.route('/logout')
def logout():
    session.pop('name', None) 
    return redirect(url_for('vamos_arrasar.login'))
