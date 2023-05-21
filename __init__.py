# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6b5f3be135504ab3c4ddfaab391c8dd7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:harrypotter@localhost/banco'
db = SQLAlchemy(app)

from projetofacu import routes
from projetofacu.models import Usuario, Turma, Grade