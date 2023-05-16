import pymysql

# Conectando ao banco de dadps
connection = pymysql.connect(host='localhost', user='root', password='', database='sisu')


def attrs_str(attrs_dict):
    

    # str_graus = 
    #     for grau in graus:
    #         if grau != '':
    #             str_graus += f'\"{grau}\", '
    #     str_graus = str_graus[:-2] + ']'
    string = ''
    for x in attrs_dict:
        lista = attrs_dict[x]
        if type(lista) == list:
            str_lista = '['
            for attr in lista:
                if attr != '':
                    str_lista += f'\"{attr}\", '
            str_lista = str_lista[:-2] + ']'
            if lista != []:
                string += f"{x} = \'{str_lista}\', "
            else:
                string += f"{x} = \'[]\', "
        
        elif type(lista) == dict:
            string += f"{x} = \'"+"{"
            for y in lista:
                string += f'\"{y}\": \"{lista[y]}\", '
            string = string[:-2] + "}\', "
    return string[:-2]


def escape_aspas(texto):
    if type(texto) == str and '"' in texto:  
        texto = texto.replace('"', r'\"')
    return texto


def executar_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)  
    connection.commit()


def lista_para_texto(lista, aspas=True):
    texto = ''
    for elem in lista:
        elem = escape_aspas(elem)
        if aspas:
            texto += f'"{elem}", '
        else:
            texto += f'{elem}, '
    return texto[:-2]


def construtor_sql_insert(tabela, colunas, dados):
    """Constroi uma string contendo código SQL para inserir um determinado dado em uma tabela"""
    sql = f"INSERT INTO {tabela} {f'({lista_para_texto(colunas, aspas=False)})' if colunas else ''} VALUES ({lista_para_texto(dados)})"
    return sql


def construtor_sql_update(tabela, attrs, where=None):
    """Constroi uma string contendo código SQL para alterar um determinado dado em uma tabela"""
    sets = attrs_str(attrs)
    sql = f"UPDATE {tabela} SET {sets} {f'WHERE {where}' if where else ''}"
    print(sql)
    return sql


def insert(tabela, coluna, dados):
    executar_sql(construtor_sql_insert(tabela, coluna, dados))


def update(tabela, attrs, where=None):
    executar_sql(construtor_sql_update(tabela, attrs, where))
    
    