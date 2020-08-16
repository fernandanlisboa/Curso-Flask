from app import app
#aplicando o método route para a função index 
#criação de uma página
@app.route("/index")
@app.route("/") #rota da minha página index
def index(): #padrão de chamada da página principal web
    return "Hello World"

@app.route("/test", defaults = {'name': None})
@app.route("/test<name>")
def teste(name): #variable default
    if name:
      return "Olá %s!" % name
    else:
        return "Olá usuário!"