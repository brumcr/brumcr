# routes.py
from flask import render_template, redirect, url_for, request, flash
from projetofacu import app, db
from projetofacu.forms import FormLogin, FormCriarConta, FormEscola, FormProfessor, FormDisciplina, FormTurma, FormGrade
from projetofacu.models import Usuario, Turma, Grade, Escola, Professor, Disciplina

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/escola", methods=['GET', 'POST'])
def escola():
    form_escola = FormEscola()
    if form_escola.validate_on_submit() and 'botao_submit_escola' in request.form:
        # Obtenha os dados do formulário
        nome = form_escola.nome.data
        logradouro = form_escola.logradouro.data
        endereco = form_escola.endereco.data
        cep = form_escola.cep.data
        ddd = form_escola.ddd.data
        telefone = form_escola.telefone.data
        email = form_escola.email.data

        # Crie um objeto Escola com os dados do formulário
        nova_escola = Escola(nome=nome, logradouro=logradouro, endereco=endereco, cep=cep, ddd=ddd, telefone=telefone,
                             email=email)

        # Adicione a nova escola ao banco de dados
        db.session.add(nova_escola)
        db.session.commit()

        flash('Nova escola adicionada com sucesso!', 'success')
        return redirect(url_for('homepage'))

    # Verifique se há erros de validação no formulário
    if form_escola.errors:
        flash('Erro de validação no formulário!', 'danger')
        print(form_escola.errors)

    return render_template("escola.html", form_escola=form_escola)

@app.route('/professor', methods=['GET', 'POST'])
def professor():
    form_professor = FormProfessor()
    if form_professor.validate_on_submit() and 'botao_submit_professor' in request.form:
        # Obtenha os dados do formulário
        nome = form_professor.nome.data
        sobrenome = form_professor.sobrenome.data
        cpf = form_professor.cpf.data
        ddd = form_professor.ddd.data
        telefone = form_professor.telefone.data
        email = form_professor.email.data

        # Crie um novo objeto Professor e adicione-o ao banco de dados
        novo_professor = Professor(nome=nome, sobrenome=sobrenome, cpf=cpf, ddd=ddd, telefone=telefone, email=email)
        db.session.add(novo_professor)
        db.session.commit()

        flash('Novo professor adicionado com sucesso!', 'success')
        return redirect(url_for('homepage'))

    if form_professor.errors:
        flash('Erro de validação no formulário!', 'danger')
        print(form_professor.errors)

    return render_template('professor.html', form_professor=form_professor)

@app.route('/disciplina', methods=['GET', 'POST'])
def disciplina():
    form_disciplina = FormDisciplina()
    if form_disciplina.validate_on_submit() and 'botao_submit_disciplina' in request.form:
        # Obtenha os dados do formulário
        nome = form_disciplina.nome.data
        carga = form_disciplina.carga.data
        cpf = form_disciplina.cpf.data

        # Crie uma nova disciplina
        nova_disciplina = Disciplina(nome=nome, carga=carga, cpf=cpf)
        db.session.add(nova_disciplina)
        db.session.commit()

        flash('Nova disciplina adicionada com sucesso!', 'success')
        return redirect(url_for('homepage'))

    # Verifique se há erros de validação no formulário
    if form_disciplina.errors:
        flash('Erro de validação no formulário!', 'danger')
        print(form_disciplina.errors)

    return render_template('disciplina.html', form_disciplina=form_disciplina)



@app.route('/turma', methods=['GET', 'POST'])
def turma():
    form_turma = FormTurma()
    if form_turma.validate_on_submit() and 'botao_submit_turma' in request.form:
        # Obtenha os dados do formulário
        nome = form_turma.nome.data
        carga = form_turma.carga.data

        # Crie uma nova turma
        nova_turma = Turma(nome=nome, carga=carga)
        db.session.add(nova_turma)
        db.session.commit()

        flash('Nova turma adicionada com sucesso!', 'success')
        return redirect(url_for('homepage'))

    # Verifique se há erros de validação no formulário
    if form_turma.errors:
        flash('Erro de validação no formulário!', 'danger')
        print(form_turma.errors)

    return render_template('turma.html', form_turma=form_turma)


@app.route('/grade', methods=['GET', 'POST'])
def grade():
    form_grade = FormGrade()

    if form_grade.validate_on_submit() and 'botao_submit_grade' in request.form:
        # Obtenha os dados do formulário
        nome = form_grade.nome.data
        dia = form_grade.dia.data
        disciplina = form_grade.disciplina.data
        professor = form_grade.professor.data

        # Verifique se os dados estão sendo recebidos corretamente
        print(f'Nome: {nome}')
        print(f'Dia: {dia}')
        print(f'Disciplina: {disciplina}')
        print(f'Professor: {professor}')

        nova_grade = Grade(nome=nome, dia=dia, disciplina=disciplina, professor=professor)
        db.session.add(nova_grade)
        db.session.commit()

        flash('Nova grade adicionada com sucesso!', 'success')
        return redirect(url_for('homepage'))

    # Verifique se há erros de validação no formulário
    if form_grade.errors:
        flash('Erro de validação no formulário!', 'danger')
        print(form_grade.errors)

    return render_template('grade.html', form_grade=form_grade)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('homepage'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        usuario_novo = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=form_criarconta.senha.data)
        db.session.add(usuario_novo)
        db.session.commit()
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('homepage'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/visualizador', methods=['GET', 'POST'])
def visualizador():
    return render_template('visualizador.html')