from flask import Blueprint,render_template,url_for,redirect, abort,request,flash

blueprint_default=Blueprint('blueprint_default', __name__)

@blueprint_default.route('/')
def index():
    return redirect(url_for('login'))

@blueprint_default.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        login=request.form['login']
        senha=request.form['senha']
        if senha=="Gata" and login=="Minha":
            return redirect(url_for('admin'))
        flash("Senha incorreta")
    return redirect(url_for('login'))

@blueprint_default.route('/admin')
def admin():
    return "Ola meu amor"

@blueprint_default.route('/rota_errada')
def rota_errada():
    abort(404) 
    return redirect(url_for('page_not_found'))


@blueprint_default.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404
