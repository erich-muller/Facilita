"""
Esse programa tem o intuito de ler as tabelas de relatório disponibilizadas pelo INEP
https://sisu.mec.gov.br/#/relatorio#onepage, coletar os dados e transformar em lista
"""
from pandas import read_excel, ExcelFile
import os
from math import isnan

def verificador_nan(n):
    try:
        n = float(n)
        return isnan(n)
    except: 
        if n == '' or n == 'nan':
            return True
        return False


def leitor_xlsx(nome_arquivo, colunas):
    """Lê determinadas colunas de um determinado arquivo excel"""
    nome_folha = ExcelFile(nome_arquivo).sheet_names[1]
    data = read_excel(nome_arquivo, nome_folha, usecols=colunas, skiprows=1, converters={col: lambda y: 0 if verificador_nan(y) else y for col in range(0, len(colunas))}).values
    return data


def listar_xlsx(path):
    """Lista todos os arquivos xlsx em um determinado diretório."""
    planilhas = [arq for arq in os.listdir(path) if arq.endswith('.xlsx')]
    return planilhas

