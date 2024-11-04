# models/Usuario.py
class Usuario:
    usuarios = {
        "admin": "1234"
    }

    @classmethod
    def autenticar(cls, username, password):
        return cls.usuarios.get(username) == password
