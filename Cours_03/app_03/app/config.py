import dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))

class Config():
    DEBUG = os.environ.get("DEBUG") #accès à la variable DEBUG situé dans .env
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")#accès à la variable désignée dans .env. Permet ainsi l'accès à la base de donnée lors du lancement de l'appli. 
