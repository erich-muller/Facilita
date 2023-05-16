from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, DateField, PasswordField, BooleanField, DecimalField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class CadastroForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    nascimento = DateField('nascimento', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class preferenciasCursoForm(FlaskForm):
    cursos = StringField('cursos', validators=[DataRequired()])
    # grau de formação
    bacharelado = BooleanField('bacharelado')
    licenciatura = BooleanField('licenciatura')
    tecnologico = BooleanField('tecnologico')
    abi = BooleanField('abi')


class preferenciasVagasForm(FlaskForm):
    # turnos
    matutino = BooleanField('matutino')
    vespertino = BooleanField('vespertino')
    noturno = BooleanField('noturno')
    integral = BooleanField('integral')
    ead = BooleanField('ead')

    # perfil do usuario
    escola_publica = BooleanField('escola_publica')
    preto_pardo = BooleanField('preto_pardo')
    indigena = BooleanField('indigena')
    deficiente = BooleanField('deficiente')
    trans_trav = BooleanField('trans_trav')
    quilombola = BooleanField('quilombola')


class notasForm(FlaskForm):
    matematica = DecimalField()
    linguagens = DecimalField()
    ciencias_natureza = DecimalField()
    ciencias_humanas = DecimalField()
    redacao = DecimalField()
