from flask import Flask 
from controllers.controller import vamos_arrasar

app = Flask(__name__)
app.register_blueprint(vamos_arrasar)
app.secret_key = 'JesusVive'  #chave para acessar os cookies da sessão para que o user não modifique o cookie|CRIPTOGRAFIA


if __name__ == '__main__':
    app.run(debug=True)





