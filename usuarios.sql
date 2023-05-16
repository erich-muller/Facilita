create database sisu;


-- Informações sobre o usuário e seus interesses

create table usuarios (
	id int not null auto_increment,
    nome varchar(30) not null,
    nascimento date not null,
    email varchar(30) not null unique,
	tipo_conta varchar(20) default 'gratis',
    cidades JSON,
    notas JSON,
    turnos JSON,
    cotas JSON,
    grau JSON,
    pendencias JSON,
    
    primary key (id)
) default charset = utf8;


select * from usuarios limit 1;