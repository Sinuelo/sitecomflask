import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = 'f25b71426615341d9f9138c716b24b8f'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para continuar'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import models


engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspection = sqlalchemy.inspect(engine)
if not inspection.has_table('post', schema='dbo'):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print('Base de Dados criada com sucesso')
else:
    print('Base de dados já existe')


from comunidadeimpressionadora import routes
