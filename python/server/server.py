from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_hashing import Hashing
from models.forms import notasForm, LoginForm, CadastroForm, preferenciasVagasForm, preferenciasCursoForm
import bd.aluno as aluno


app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(_id):
    return aluno.Aluno(_id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login_page'))

hashing = Hashing(app)


# ------------------ PÁGINAS ----------------------

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/pendencias")
def pendencias_page():
    user = aluno.Aluno(current_user.get_id())
    print(user.pendencias)
    if user.pendencias != []:
        return redirect(url_for(user.pendencias[0], next='pendencias'))
    else:
        return redirect(url_for('home'))


@app.route("/login", methods=['POST', 'GET'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        email, senha = form.email.data, form.senha.data
        _id = aluno.buscar(email=email)[0]
        user = aluno.Aluno(_id)
        if hashing.check_value(user.senha, senha):
            login_user(user)
            print('Usuário Logado')
            return redirect(url_for('pendencias_page'))
    return render_template('login.html', form=form)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_page():
    form = CadastroForm()
    if form.validate_on_submit():
        nome, nascimento, email, senha = form.nome.data, form.nascimento.data, form.email.data, form.senha.data
        senha_hash = hashing.hash_value(senha)
        if aluno.registrar(nome, nascimento, email, senha_hash):
            print('Aluno registrado!')
            
        return redirect(url_for('login_page'))
        
    return render_template('cadastro.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/preferencias_curso', methods=['POST', 'GET'])
@login_required
def preferencias_curso():
    form = preferenciasCursoForm()
    user = aluno.Aluno(current_user.get_id())

    if form.validate_on_submit():
        cursos = form.cursos.data.split(',')
        bacharelado, licenciatura = form.bacharelado.data, form.licenciatura.data
        tecnologico, abi = form.tecnologico.data, form.abi.data
        
        # Atualizando no banco de dados
        graus = ["Licenciatura" if licenciatura else "", "Bacharelado" if bacharelado else "", "Tecnológico" if tecnologico else "", "Área Básica de Ingresso (ABI)" if abi else ""]
        
        # Remover pendencia
        pendencias = user.pendencias

        if 'preferencias_curso' in pendencias:
            pendencias.remove('preferencias_curso')
        dados = {
            'cursos': cursos,
            'grau': graus,
            'pendencias': pendencias
        }
        
        user.alterar(dados)

        return redirect(request.args.get("next") or url_for('home'))
    
    graus = user.grau
    dados = {'bacharelado': True if 'Bacharelado' in graus else False,
             'licenciatura': True if 'Licenciatura' in graus else False,
             'tecnologico': True if 'Tecnológico' in graus else False,
             'abi': True if 'Área Básica de Ingresso (ABI)' in graus else False}
    return render_template('dados_compl_1.html', form=form, cursos=user.cursos, dados=dados)


@app.route('/preferencias_vagas', methods=['GET', 'POST'])
@login_required
def preferencias_vagas():
    form = preferenciasVagasForm()
    user = aluno.Aluno(current_user.get_id())
    
    if form.validate_on_submit():
        matutino = form.matutino.data
        vespertino = form.vespertino.data
        noturno = form.noturno.data
        integral = form.integral.data
        ead = form.ead.data

        escola_publica = form.escola_publica.data
        preto_pardo = form.preto_pardo.data
        indigena = form.indigena.data
        deficiente = form.deficiente.data
        trans_trav = form.trans_trav.data
        quilombola = form.quilombola.data

        print(matutino, vespertino, noturno, integral, ead)
        print(escola_publica, preto_pardo, indigena, deficiente, trans_trav, quilombola)
        
        turnos = ["Matutino" if matutino else "", "Vespertino" if vespertino else "", "Noturno" if noturno else "", "Integral" if integral else "", "EaD" if ead else ""]
        cotas = ["Escola Pública" if escola_publica else "", "Preto ou Pardo" if preto_pardo else "", "Indígena" if indigena else "", "Deficiente" if deficiente else "", "Transexual, Transgênero ou Travesti" if trans_trav else "", "Quilombola" if quilombola else ""]
        
        pendencias = user.pendencias
        if 'preferencias_vagas' in pendencias:
            pendencias.remove('preferencias_vagas')

        dados = {
            'turnos': turnos,
            'cotas': cotas,
            'pendencias': pendencias
        }

        user.alterar(dados)

        return redirect(request.args.get("next") or url_for('home'))

    cotas = user.cotas
    turnos = user.turnos
    dados = {'escola_publica': True if 'Escola pública' in cotas else False,
             'preto_pardo': True if 'Preto ou Pardo' in cotas else False,
             'indigena': True if 'Índigena' in cotas else False,
             'deficiente': True if 'Deficiente' in cotas else False,
             'trans_trav': True if 'Transexual, Transgênero ou Travesti' in cotas else False,
             'quilombola': True if 'Quilombola' in cotas else False,
             
             'matutino': True if 'Matutino' in turnos else False,
             'vespertino': True if 'Vespertino' in turnos else False,
             'noturno': True if 'Noturno' in turnos else False,
             'integral': True if 'Integral' in turnos else False,
             'ead': True if 'EaD' in turnos else False,
             }

    return render_template('dados_compl_2.html', form=form, dados=dados)


@app.route('/preferencias_notas', methods=['POST', 'GET'])
@login_required
def preferencias_notas():
    form = notasForm()
    user = aluno.Aluno(current_user.get_id())

    if form.validate_on_submit():
        matematica = form.matematica.data
        linguagens = form.linguagens.data
        ciencias_natureza = form.ciencias_natureza.data
        ciencias_humanas = form.ciencias_humanas.data
        redacao = form.redacao.data

        pendencias = user.pendencias
        if 'preferencias_notas' in pendencias:
            pendencias.remove('preferencias_notas')

        dados = {
            'notas': {'Matemática': matematica, 'Linguagens': linguagens,
                      'Ciências Natureza': ciencias_natureza, 'Ciências Humanas': ciencias_humanas,
                      'Redação': redacao},
            'pendencias': pendencias
        }

        user.alterar(dados)
        return redirect(request.args.get("next") or url_for('home'))

    return render_template('dados_notas.html', form=form, dados=user.notas)


@app.route('/meuperfil')
@login_required
def perfil_user():
    user = aluno.Aluno(current_user.get_id())
    user = user.nome, user.email
    return render_template('user.html', dados=user)


@app.route('/meusdados')
@login_required
def dados_pessoais():
    pass


app.run()
