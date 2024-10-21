from flask import Flask, render_template
from controllers import contatos_blueprint
app = Flask(__name__)
app.register_blueprint(contatos_blueprint)

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)