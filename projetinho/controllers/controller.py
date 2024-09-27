from flask import Blueprint, render_template, request, redirect, url_for
from model.models import Livro, AddLivros, listaLivros

vamos_arrasar = Blueprint('ListaLivros', __name__)

@vamos_arrasar.route('/')
def visu():
    return render_template ('index.html', listaLivros=listaLivros)

@vamos_arrasar.route('/add', methods=['POST'])
def add():
    nome = request.form ['nome']
    autor = request.form ['autor']
    gosto = request.form ['gosto']
    AddLivros(nome, autor, gosto)
    return redirect(url_for('ListaLivros.visu'))