create database inscricoes_sisu
default character set utf8
default collate utf8_general_ci;

use inscricoes_sisu;

create table inscricoes (
	# INFOS COMUNS AOS DOIS BANCOS DE DADOS
    
	# NU_ANO smallint,
    # NU_EDICAO tinyint,
    # CO_IES int,
    # NO_IES varchar(120),
    # SG_IES varchar(12),
    # DS_ORGANIZACAO_ACADEMICA varchar(60),
    # DS_CATEGORIA_ADM varchar(25),
    # NO_CAMPUS varchar(100),
    # NO_MUNICIPIO_CAMPUS varchar(40),
    # SG_UF_CAMPUS varchar(2),
    # DS_REGIAO_CAMPUS varchar(15),
    # CO_IES_CURSO varchar(10),
    # NO_CURSO varchar(80),
    # DS_GRAU varchar(15),
    # DS_TURNO varchar(10),
    TP_MODALIDADE varchar(80),
    DS_MOD_CONCORRENCIA varchar(400),
    NU_PERCENTUAL_BONUS decimal(4,2),
    QT_VAGAS_CONCORRENCIA smallint,
    NU_NOTACORTE decimal(5,2),
    QT_INSCICAO int
) default charset = utf8;

drop table inscricoes;