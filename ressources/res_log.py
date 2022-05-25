from flask_restful import Resource,reqparse
from models.mod_log import LogModel
from flask_jwt import jwt_required, current_identity
from time import time

class ResLog(Resource):   
    #Mise en place du parser
    parser = reqparse.RequestParser()
    parser.add_argument('id',type=int,help='Fournir l\'id du log',location='args')
    parser.add_argument('message', type =str, help='Fournir le message du log', location='json')
    parser.add_argument('id_cat', type =str, help='Fournir l\'id de la catégorie', location='json')
    
    
    @classmethod
    def get(cls):
        #cls.parser.remove_argument('message')
        args = cls.parser.parse_args()
        if args['id'] is None :
             return {'Erreur':'Fournissez un id'}, 400
        #On accède au modèle pour récupérer le log
        log = LogModel.find_by_logid(args['id'])
        #On convertit le log en json pour la réponse
        return log.json(),200
        
    @jwt_required()
    def post(self):
        user = current_identity.username
        args = ResLog.parser.parse_args()
        if args['message'] is None :
             return {'Erreur':'Fournissez un message'}, 400
        #Création d'un objet log en base
        log = LogModel(args['message'], user,args['id_cat'])
        log.save_to_db()
        return log.json(),201
    
    @jwt_required()
    def put(self):
        user = current_identity.username
        args = ResLog.parser.parse_args()
        if args['id'] is None :
            return {'Erreur':'Fournissez un id'}, 400
        if args['message'] is None :
            return {'Erreur':'Fournissez un message'}, 400
        #Récupération du log
        log = LogModel.find_by_logid(args['id'])
        #Modification du log
        log.msg = args['message']
        log.user = user
        log.timestamp = str(time())
        log.save_to_db()
        return log.json(),200
    
    @jwt_required()
    def delete(self):
        #Pas besoin du body
        ResLog.parser.remove_argument('message')
        args = ResLog.parser.parse_args()
        if args['id'] is None :
            return {'Erreur':'Fournissez un message'}, 400
        log = LogModel.find_by_logid(args['id'])
        log.delete_from_db()
        return {"":""},204