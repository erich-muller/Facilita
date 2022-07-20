import pymysql

# Conectando ao banco de dadps
connection = pymysql.connect(host='localhost', user='root', password='', database='inscricoes_sisu')


def lista_para_texto(lista, crase=True):
    texto = ''
    for elem in lista:
        if crase:
            texto += f'`{elem}`, '
        else:
            texto += f"'{elem}', "
    
    return texto[:-2]


def construtor_sql(tabela, colunas, dados):
    sql = f"INSERT INTO {tabela} ({lista_para_texto(colunas)}) VALUES ({lista_para_texto(dados, crase=False)})"
    return sql


def insert(tabela, coluna, dados):
    cursor = connection.cursor()
    sql = construtor_sql(tabela, coluna, dados)
    cursor.execute(sql)  
    connection.commit()
    
