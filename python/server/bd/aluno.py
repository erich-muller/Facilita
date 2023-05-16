from bd.database_inject import insert, update
from bd.database_consult import request
from flask_login import UserMixin

# from database_inject import insert, update
# from database_consult import request
import json


def registrar(nome, nascimento, email, senha):
    try:
        insert('usuarios', ['nome', 'nascimento', 'email', 'senha', 'pendencias'], [nome, nascimento, email, senha, '["preferencias_curso", "preferencias_vagas", "preferencias_notas"]'])
        return True
    except Exception as e:
        if 'Duplicate entry' in str(e):
            print('Já existe uma conta com este email.')
        else:
            print(e)
        return False

def buscar(_id=None, email=None):
    return request('*', 'usuarios', f'id = {_id}' if _id else f"email = '{email}'", limit=1)


class Aluno(UserMixin):
    """Acessar e escrever informações sobre o aluno"""

    # @property
    # def is_authencticated(self):
    #     return True
    
    # @property
    # def is_active(self):
    #     return True

    # @property
    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     return str(self.id)

    def __init__(self, _id):
        dados = buscar(_id)
        self.dados = dados
        self.id = dados[0]
        self.nome = dados[1]
        self.nascimento = dados[2]
        self.email = dados[3]
        self.senha = dados[4]

        self.tipo_conta = dados[5]
        self.cursos = json.loads(dados[6])
        self.cidades = json.loads(dados[7])
        self.notas = json.loads(dados[8])
        self.turnos = json.loads(dados[9])
        self.cotas = json.loads(dados[10])
        self.grau = json.loads(dados[11])
        self.pendencias = json.loads(dados[12])


    def alterar(self, attrs):
        # Exemplo de uso: aluno.alterar({'cidades': '["Nova Friburgo", "Florestal", "Ouro Preto"]'})
        update('usuarios', attrs, f'id = {self.id}')

    def descricao(self):
        # Traz uma descrição resumida e em linguagem humana sobre o aluno
        print(f'O aluno {self.nome} (id={self.id}), nascido em {self.nascimento}, possui uma conta {self.tipo_conta}. Suas cidades de interesse são {self.cidades}\n', f'pendências: {self.pendencias}')
        # print(self.dados)


"""attrs = {
'cidades': '["Nova Friburgo", "Florestal", "Rio de Janeiro"]',
'turnos': '["Vespertino", "Matutino", "Integral"]',
'grau': '["Licenciatura", "Área Básica de Ingresso (ABI)"]'
}

q2 = {
'cursos': '["Matemática", "História"]'
}

erich = Aluno(1)
erich.alterar(q2)
"""

# erich = Aluno(2)

# print(erich.pendencias, type(erich.pendencias))
# print(buscar())