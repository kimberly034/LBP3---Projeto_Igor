from flask import Flask
from controller.geralController import geral_bp
from controller.loginController import login_bp

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Registra os Blueprints
app.register_blueprint(geral_bp)
app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(debug=True)
