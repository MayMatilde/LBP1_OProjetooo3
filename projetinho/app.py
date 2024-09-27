from flask import Flask, render_template, redirect, url_for, request
from controllers.controller import vamos_arrasar

app = Flask(__name__)
app.register_blueprint(vamos_arrasar)

if __name__ == '__main__':
    app.run(debug=True)