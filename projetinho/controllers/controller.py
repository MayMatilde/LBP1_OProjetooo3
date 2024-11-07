from flask import Blueprint, render_template, request, redirect, session, url_for, flash, make_response
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
                return redirect(url_for('vamos_arrasar.resposta')) #renderiza a função resposta, porque deu certo
        flash('Usuário ou senha inválidos!', 'erro')
    return render_template('index.html')

#A rota que deu certo  😉
@vamos_arrasar.route('/resposta', methods=["GET", "POST"])
def resposta():
    if request.method == "POST":
        response = make_response(redirect(url_for('vamos_arrasar.resposta')))
        if request.form.get('opcao1'):
            response.set_cookie("versiculo", "Um novo mandamento vos dou: Que vos ameis uns aos outros. (João 13:34-35)", max_age=60 * 60 * 24)
        elif request.form.get('opcao2'):
            response.set_cookie("versiculo", "Deixo-lhes a paz; a minha paz lhes dou. (João 14:27)", max_age=60 * 60 * 24)
        elif request.form.get('opcao3'):
            response.set_cookie("versiculo", "E eu estarei sempre com vocês, até o fim dos tempos. (Mateus 28:20)", max_age=60 * 60 * 24)
        elif request.form.get('opcao4'):
            response.set_cookie("versiculo", "Vinde a mim, todos os que estais cansados e oprimidos, e eu vos aliviarei. (Mateus 11:28-30)", max_age=60 * 60 * 24)
        return response

    versiculo = request.cookies.get('versiculo', "Nenhum versículo foi selecionado.")
    return render_template("resposta.html", versiculo=versiculo)


#Rota logout😁
@vamos_arrasar.route('/logout')
def logout():
    resp= make_response(redirect(url_for("vamos_arrasar.login")))
    session.pop('name', None) 
    resp.set_cookie("versiculo1", "", expires = 0)
    resp.set_cookie("versiculo2", "", expires = 0)
    resp.set_cookie("versiculo3", "", expires = 0)
    resp.set_cookie("versiculo4", "", expires = 0)
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