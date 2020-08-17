from flask import render_template
from app import app
from app.models.tables import User
from app.models.forms import LoginForm
#aplicando o método route para a função index 
#criação de uma página
@app.route("/index/<user>" )
@app.route("/", defaults={"user": None}) #rota da minha página index
def index(user): #padrão de chamada da página principal web
    return render_template('index.html',
                           user = user) #recebe um arquivo html
    
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template('login.html',
                               form = form)

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = User("fernandinha", "1234", "Fernanda Lisboa", "fernandinha@mail.com")
    db.session.add(i)
    db.session.commit() #salvamento de informações da sessão