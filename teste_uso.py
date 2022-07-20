from data_reader import leitor
from database_inject import *


planilha = 'planilhas/2019_2.xlsx'
folha = 'inscricao_2019_2'
colunas = ['NU_ANO', 'NU_EDICAO', 'CO_IES', 'NO_IES', 'SG_IES', 'DS_ORGANIZACAO_ACADEMICA', 'DS_CATEGORIA_ADM', 'NO_CAMPUS', 'NO_MUNICIPIO_CAMPUS', 'SG_UF_CAMPUS', 'DS_REGIAO_CAMPUS', 'CO_IES_CURSO', 'NO_CURSO', 'DS_GRAU', 'DS_TURNO']

def teste_leitor(a, b):
    for x in range(a, b):
        print(leitor(planilha, folha, x, colunas))


def teste_database_inject(a, b):
    for x in range(a, b):
        print(f"Em andamento... ({a}/{b})", end='\r')
        dados = leitor(planilha, folha, x, colunas)
        insert('dados_base', colunas, dados)


# teste_leitor(2, 10)
teste_database_inject(2, 11943)
""" FUNCIONA, entretanto os dados estão repetidos"""
