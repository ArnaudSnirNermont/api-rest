import os
from db import db
from datetime import timedelta
from flask import Flask
from flask_restful import Api
from ressources.res_log import ResLog
from ressources.res_loglist import ResLogList
from ressources.res_categorielist import ResCategories
from ressources.res_user import ResUserRegister 
from ressources.res_categorie import ResCategorie
from flask_jwt import JWT
from securite import authentification, identity


#Création d'une app flash
app = Flask(__name__)
#Création d'un API basé sur flask_restful et sur l'APP flask
api = Api(app)
app.secret_key = "arnaud"

#Config SQLAlchemy
#Type de bdd et emplacement
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL2","sqlite:///data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
 

#Gestion du JWT
#Changement de la route d'authentification (par defaut : /auth)
app.config['JWT_AUTH_URL_RULE'] = '/login'
# changement de la durée avant expiration du token
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
#la config de JWT doit être éventuellement changée AVANT la création de l'instance
jwt = JWT(app, authentification,identity)

#Définition des endpoints : ajout de la ressource à l'API
#Association entre l'API flask_restful, la classe de traitement et la route (endpoint)
api.add_resource(ResLogList,'/logs')
api.add_resource(ResLog,'/log')
api.add_resource(ResUserRegister,'/register')
api.add_resource(ResCategorie,'/categorie')
api.add_resource(ResCategories,'/categories')

if __name__ == "__main__":
    #programme de test
    #Démarrage de flask_sqlalchemy
    db.init_app(app)
    # #lancement de l'app flask
    app.run(debug=True,port='9999')
    