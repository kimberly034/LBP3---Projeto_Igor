# controllers/loginController.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from model.usuario import Usuario

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simulação de autenticação
        if Usuario.autenticar(username, password):
            session['username'] = username
            return redirect(url_for('geral.index'))
        else:
            flash('Usuário ou senha incorretos')
    return render_template('login.html')

@login_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.login'))
