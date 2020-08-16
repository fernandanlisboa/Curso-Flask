from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' #configuração do banco -> uri de conexão do banco de dados
db = SQLAlchemy(app)

from app.controllers import default