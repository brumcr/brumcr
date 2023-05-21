# meu_site.py
from projetofacu import app, db

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

# servidor do heroku
# Criar um arquivo em txt para incluir a documentação / Procfile

# Criar o file Procfile
# Para criar a documentação pip install requirements.txt
# heroku login
# git init
#git config --global user.email "brunalopescorreia@gmail.com"
#git config --global user.name "Brumcr"
#git init
#heroku git:remote -a siteestudantesunivesp
#================================ PARA ATUALIZAR PRECISA
#$ heroku login
#$ git add .
#$ git commit -am "maio 9"
#$ git push heroku master

# MODULO DE SEGURANÇA
# TERMINAL - import secrets
# TERMINAL - secrets.token_hex(16)
# TERMINAL - copiar token passado
# TERMINAL - exit() // Fechar python

# pip install flask-wtf
# pip install email_validator