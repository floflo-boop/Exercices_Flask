from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy #importer l'ORM SQLAlchemy

app = Flask(
    __name__, 
    template_folder='templates',
    static_folder='statics')
app.config.from_object(Config)

db = SQLAlchemy(app) #j'instancie db en reliant l'ORM à mon application. Cela donne la base afin de relier la base, faire des models, etc.

from .routes import generales