from flask import Flask, render_template, session, redirect, url_for, request, make_response
from controllers.controller import vamos_arrasar

app = Flask(__name__)
app.register_blueprint(vamos_arrasar)
app.secret_key = 'JesusVive'  #chave para acessar os cookies da sessão para que o user não modifique o cookie|CRIPTOGRAFIA

rotas_livres = ["vamos_arrasar.visu", "vamos_arrasar.login"]


@app.before_request
def porteiroDaSessao():
    if request.endpoint in rotas_livres:
        return


if __name__ == '__main__':
    app.run(debug=True)
