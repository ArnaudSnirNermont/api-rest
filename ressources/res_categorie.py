from flask_restful import Resource, reqparse
from models.mod_categorie import CategorieModel

class ResCategorie(Resource):
    
    #Mise en place du parser
    parser = reqparse.RequestParser()
    parser.add_argument('id',type=int,help='Fournir l\'id de la catégorie',location='args')
    parser.add_argument('nom', type =str, help='Fournir le nom de la catégorie', location='json')
    
    @classmethod
    def get(cls):
        args = cls.parser.parse_args()
        categorie = CategorieModel.find_by_catid(args['id'])
        return categorie.json()
    
    @classmethod
    def post(cls):
        args= cls.parser.parse_args()
        categorie = CategorieModel(args['nom'])
        categorie.save_to_db()
        return categorie.json(),201
    
    @classmethod
    def put(cls):
        args= cls.parser.parse_args()
        categorie = CategorieModel.find_by_catid(args['id'])
        categorie.nom_cat= args['nom']
        categorie.save_to_db()
        return categorie.json(),200
    

    
