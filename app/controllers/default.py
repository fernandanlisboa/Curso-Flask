from flask import render_template
from app import app
#aplicando o método route para a função index 
#criação de uma página
@app.route("/index/<user>" )
@app.route("/", defaults={"user": None}) #rota da minha página index
def index(user): #padrão de chamada da página principal web
    return render_template('base.html',
                           user = user) #recebe um arquivo html
    
@app.route("/login")
def login():
      return render_template('base.html')
