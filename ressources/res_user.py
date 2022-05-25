import sqlite3
from flask_restful import Resource,reqparse
from models.mod_user import UserModel


class ResUserRegister(Resource):
    #Mise en place du parser
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='veuillez obligatoirement remplir ce champ')
    parser.add_argument('password', type=str,required=True,help='veuillez obligatoirement remplir ce champ') 

    def post(self):   
        data_body = ResUserRegister.parser.parse_args()
        #Vérif si le user existe
        if UserModel.find_by_username(data_body['username']) :
            return {'message': 'Utilisateur déjà existant'},400
        #user= UserModel(data_body['username'],data_body['password'])
        #On sait grâce au parser qu'on aura les bons éléments
        user= UserModel(**data_body)
        user.save_to_db()
        return {'message': 'Utilisateur créé avec succès'},201