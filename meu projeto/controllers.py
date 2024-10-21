# controllers.py
from flask import Blueprint, render_template, request, redirect, url_for
# Criação do blueprint para modularizar as rotas
contatos_blueprint = Blueprint('contatos', __name__)
@contatos_blueprint.route('/')
def index():    
    return redirect(url_for('contatos.login'))
@contatos_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        login = request.form['login']
        senha = request.form['senha']
        if senha =='2024' and login == 'dotosa':
            return redirect(url_for('contatos.sucesso'))
        return redirect(url_for('contatos.login'))
    return render_template("login.html")

@contatos_blueprint.route('/sucesso')
def sucesso():
    return "sucesso"

#@contatos_blueprint.route('/')
#def login():
#    if request.method == 'POST':
#
#        login = request.form['login']
#        senha = request.form['senha']
#        if senha =='2024' and login == 'dotosa':
#            return redirect(url_for('sucesso'))
#    return redirect(url_for('contatos_login'))




