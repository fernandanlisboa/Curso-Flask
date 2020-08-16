from app import app
#aplicando o método route para a função index 
#criação de uma página
@app.route("/") #rota da minha página index
def index(): #padrão de chamada da página principal web
    return "Hello World"