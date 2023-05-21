# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')

class FormEscola(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    logradouro = StringField('Logradouro', validators=[DataRequired()])
    endereco = StringField('Endereço', validators=[DataRequired()])
    cep = StringField('CEP', validators=[DataRequired()])
    ddd = StringField('DDD', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    botao_submit_escola = SubmitField('Salvar')

class FormProfessor(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    ddd = StringField('DDD', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    botao_submit_professor = SubmitField('Salvar')

class FormDisciplina(FlaskForm):
    nome = StringField('Nome da Disciplina', validators=[DataRequired()])
    carga = StringField('Carga Horária', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    botao_submit_disciplina = SubmitField('Salvar')

class FormTurma(FlaskForm):
    nome = StringField('Nome da Disciplina', validators=[DataRequired()])
    carga = StringField('Carga Horária Obrigatória', validators=[DataRequired()])
    botao_submit_turma = SubmitField('Salvar')

class FormGrade(FlaskForm):
    nome = StringField('Nome da Turma', validators=[DataRequired()])
    dia = StringField('Dia da Semana', validators=[DataRequired()])
    disciplina = StringField('Nome da Disciplina', validators=[DataRequired()])
    professor = StringField('Nome do Professor', validators=[DataRequired()])
    botao_submit_grade = SubmitField('Salvar')