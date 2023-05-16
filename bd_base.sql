create database adesao_sisu
default character set utf8
default collate utf8_general_ci;

use inscricoes_sisu;

create table dados_base (
	-- INFORMAÇÕES SOBRE FACULDADES, CAMPUS, REGIÕES, etc.
    ID int not null auto_increment,
    NU_ANO smallint,
    NU_EDICAO tinyint,
    CO_IES int,
    NO_IES varchar(120),
    SG_IES varchar(25),
    DS_ORGANIZACAO_ACADEMICA varchar(60),
    DS_CATEGORIA_ADM varchar(25),
    NO_CAMPUS varchar(100),
    NO_MUNICIPIO_CAMPUS varchar(40),
    SG_UF_CAMPUS varchar(2),
    DS_REGIAO_CAMPUS varchar(15),
    CO_IES_CURSO varchar(10) unique,
    NO_CURSO varchar(120),
    DS_GRAU varchar(30),
    DS_TURNO varchar(10),
    primary key (id)
) default charset = utf8;

select count(ID) from dados_base;
select * from dados_base;

select * from dados_base where NU_ANO = 2021 order by CO_IES_CURSO;

select * from dados_base where NO_CURSO = 'QUÍMICA' and CO_IES = 1811;

drop table dados_base;

truncate dados_base;
