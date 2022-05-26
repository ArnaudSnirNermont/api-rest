import imp
from app import app
from db import db

db.init_app(app)

@app.before_first_request
#Création de la BDD et des tables à moins qu'elles n'existent déjà
def create_table():
    db.create_all()