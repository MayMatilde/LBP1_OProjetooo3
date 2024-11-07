from flask import Flask, request 
from controllers.controller import vamos_arrasar

app = Flask(__name__)
app.register_blueprint(vamos_arrasar)
app.secret_key = 'JesusVive'  #chave para acessar os cookies da sessão para que o user não modifique o cookie|CRIPTOGRAFIA

rotas_livres = ["vamos_arrasar.user", "vamos_arrasar.index"]

#Middleware com o tipo before_request. Antes da requisição 
@app.before_request
def verificaSessao():
    if request.endpoint in rotas_livres:
        return


if __name__ == '__main__':
    app.run(debug=True)





