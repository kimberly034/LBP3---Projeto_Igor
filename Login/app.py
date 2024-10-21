from flask import Flask
from controllers.controller import blueprint_default as page
app=Flask(__name__)
app.register_blueprint(page)


if __name__=='__main__':
    app.run(debug=True)