from flask_restful import Resource
from models.mod_categorie import CategorieModel

class ResCategories(Resource):
    
    def get(self):
        return {"Catégories" : [categorie.json() for categorie in CategorieModel.query.all()]},200