from bd.database_consult import request


class Vaga():
    def __init__(self, dados):
        self.dados = dados
        self.NU_ANO = dados[0]
        self.NU_EDICAO = dados[1]
        self.CO_IES = dados[2]
        self.NO_IES = dados[3]
        self.SG_IES = dados[4]
        self.DS_ORGANIZACAO_ACADEMICA = dados[5]
        self.DS_CATEGORIA_ADM = dados[6]
        self.NO_CAMPUS = dados[7]
        self.NO_MUNICIPIO_CAMPUS = dados[8]
        self.SG_UF_CAMPUS = dados[9]
        self.DS_REGIAO_CAMPUS = dados[10]
        self.CO_IES_CURSO = dados[11]
        self.NO_CURSO = dados[12]
        self.DS_GRAU = dados[13]
        self.DS_TURNO = dados[14]
        self.TP_MOD_CONCORRENCIA = dados[15]
        self.DS_MOD_CONCORRENCIA = dados[16]
        self.NU_PERCENTUAL_BONUS = dados[17]
        self.QT_VAGAS_CONCORRENCIA = dados[18]
        self.NU_NOTACORTE = dados[19]
        self.QT_INSCRICAO = dados[20]

    def descrever(self):
        print(f"""Edição: {self.NU_ANO}.{self.NU_EDICAO} | Curso: {self.NO_CURSO} ({self.DS_GRAU}) | Turno: {self.DS_TURNO}
        Ofertado em {self.NO_CAMPUS} ({self.SG_IES}), {self.NO_MUNICIPIO_CAMPUS} - {self.SG_UF_CAMPUS}
        Tipo de concorrência: {self.TP_MOD_CONCORRENCIA} | Nota de corte: {self.NU_NOTACORTE}
        """)



class Filtros():
    def __init__(self, args=None) -> None:
        self.args = args
        self.sql = None

    def do_usuario(self, aluno_obj) -> list:
        # Recebe um objeto Aluno e aplica suas preferências no filtro
        attrs = {
            'NO_CURSO': aluno_obj.cursos,
            'NO_MUNICIPIO_CAMPUS': aluno_obj.cidades, 
            'DS_TURNO': aluno_obj.turnos,
            'DS_GRAU': aluno_obj.grau
        }
        self.args = attrs

    def construir_sql(self) -> str:
        sql = ''
        for arg in self.args:
            
            # Se o campo de busca não for vazio 
            if self.args[arg] != None:
                sql += arg + ' IN '
                sql += '('+str(self.args[arg])[1:-1]+')'
                sql += ' AND '
        
        self.sql = sql[:-5]

    def coletar_vagas(self) -> list:
        try:
            return request('*', 'inscricoes', self.sql, order_by='NU_NOTACORTE', limit=50)

        except Exception as e:
            print('Erro:', e)
            return []

'''
filtros = Filtros()
erich = Aluno(1)

filtros.do_usuario(erich)
filtros.construir_sql()
vagas = filtros.coletar_vagas()

for vaga in vagas:
    v = Vaga(vaga)
    v.descrever()
    print()'''

