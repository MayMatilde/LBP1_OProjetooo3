from flask import Flask, session, redirect, url_for, request, render_template
from controllers.controller import vamos_arrasar

app = Flask(__name__)
app.register_blueprint(vamos_arrasar)
app.secret_key = 'JesusVive'


if __name__ == '__main__':
    app.run(debug=True)
