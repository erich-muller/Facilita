from re import L
from planilhas.data_reader import leitor_xlsx, listar_xlsx
from bd.database_inject import *
from bd.database_consult import request


# Nomes das colunas a serem usadas no banco de dados para ler as tabelas de vagas
colunas_vagas_str = ['NU_ANO', 'NU_EDICAO', 'CO_IES', 'NO_IES', 'SG_IES', 'DS_ORGANIZACAO_ACADEMICA', 'DS_CATEGORIA_ADM', 'NO_CAMPUS', 'NO_MUNICIPIO_CAMPUS', 'SG_UF_CAMPUS', 'DS_REGIAO', 'CO_IES_CURSO', 'NO_CURSO', 'DS_GRAU', 'DS_TURNO', 'DS_PERIODICIDADE', 'QT_SEMESTRE', 'QT_VAGAS_OFERTADAS', 'NU_PERCENTUAL_BONUS', 'TP_MODALIDADE', 'DS_MOD_CONCORRENCIA', 'PESO_REDACAO', 'NOTA_MINIMA_REDACAO', 'PESO_LINGUAGENS', 'NOTA_MINIMA_LINGUAGENS', 'PESO_MATEMATICA', 'NOTA_MINIMA_MATEMATICA', 'PESO_CIENCIAS_HUMANAS', 'NOTA_MINIMA_CIENCIAS_HUMANAS', 'PESO_CIENCIAS_NATUREZA', 'NOTA_MINIMA_CIENCIAS_NATUREZA', 'NU_MEDIA_MINIMA_ENEM']
# Representa a posição das colunas acima nas tabelas de vagas
colunas_vagas_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

# Nomes das colunas a serem usadas no banco de dados para a]ler as tabelas de inscricoes
colunas_inscricoes_str = ['NU_ANO', 'NU_EDICAO', 'CO_IES_CURSO', 'DS_TURNO', 'DS_MOD_CONCORRENCIA', 'NU_NOTACORTE', 'QT_INSCRICAO']
# Representa a posição das colunas acima nas tabelas de inscricao
colunas_inscricoes_num = [0, 1, 11, 14, 16, 19, 20] 

# Diretórios e arquivos usados no programa
path = './planilhas'
logvagas = 'log_vagas.txt'
loginscricoes = 'log_inscricoes.txt'


def log_planilha(planilha, logfile):
    """Registra planilhas já lidas"""
    with open(logfile, 'a') as logobject:
        logobject.write(f'{planilha}\n')


def log_consult(logfile):
    """Consulta quais planilhas já foram lidas"""
    try:
        with open(logfile, 'r') as logobject:
            return [x.strip() for x in logobject.readlines()]
    except FileNotFoundError:
        return []


def teste_database_vagas_inject():
    print('\nIniciando!')
    
    # Injeta os dados de cada planilha não lida no bd.
    for planilha in [x for x in listar_xlsx(path+'/vagas/') if x not in log_consult(logvagas)]:
        
        # Print bonitinho do log :)
        if planilha == [x for x in listar_xlsx(path+'/inscricoes/') if x not in log_consult(logvagas)][-1]:
            print(f'\t└─ Lendo planilha {planilha}')
        else:
            print(f'\t├─ Lendo planilha {planilha}')
        
        # Pega todos os dados de uma planilha.
        dados = leitor_xlsx(path+'/vagas/'+planilha, colunas_vagas_num)  
        
        # Insere todos os dados no bd.
        insert_dados_base("vagas", dados, colunas_vagas_str)

        # Faz o log da planilha lida
        log_planilha(planilha, logvagas)
            
    print('\t└─ Concluído!')


def teste_database_inscricoes_inject():
    print('\nIniciando!')

    # Injeta as informações de nota de corte e quantidade de inscição de 
    # cada planilha de inscrição no dado de vaga correspondente 
    for planilha in [x for x in listar_xlsx(path+'/inscricoes/') if x not in log_consult(loginscricoes)]:

        # Print bonitinho do log :)
        if planilha == [x for x in listar_xlsx(path+'/inscricoes/') if x not in log_consult(loginscricoes)][-1]:
            print(f'\t└─ Lendo planilha {planilha}')
        else:
            print(f'\t├─ Lendo planilha {planilha}')

        dados = leitor_xlsx(path+'/inscricoes/'+planilha, colunas_inscricoes_num)
        update_dados_base(dados)
    
    print('\t└─ Concluído!')


teste_database_inscricoes_inject()
#teste_database_vagas_inject()
#teste_database_inscricoes_inject()