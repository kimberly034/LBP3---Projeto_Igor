# models.py
class Contato:
    def __init__(self, nome, telefone, email, data_nascimento):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
# Lista de contatos em memória
contatos = []
def adicionar_contato(nome, telefone, email, data_nascimento):
 novo_contato = Contato(nome, telefone, email, data_nascimento)
 contatos.append(novo_contato)
def editar_contato(index, nome, telefone, email, data_nascimento):
    contatos[index].nome = nome
    contatos[index].telefone = telefone
    contatos[index].email = email
    contatos[index].data_nascimento = data_nascimento
def excluir_contato(index):
    if 0 <= index < len(contatos):
        contatos.pop(index)
def obter_contatos():
    return contatos
def obter_contato(index):
    if 0 <= index < len(contatos):
        return contatos[index]
    return None