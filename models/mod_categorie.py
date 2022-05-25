from db import db
from models.mod_log import LogModel

class CategorieModel(db.Model):

    #SQLAlchemy
    __tablename__ = "categories" #association avec la table de la BDD
    #Détail des colonnes
    id = db.Column(db.Integer, primary_key= True)
    nom_cat = db.Column(db.String(150))
    #logs = db.relationship(LogModel)
    
    def __init__(self,nom_cat):
        self.nom_cat = nom_cat
        

    def json(self):
        #contruit une représentation json de l'objet log
        return {"id":self.id, "nom":self.nom_cat}
        
    def save_to_db(self) :
        #Insertion ou update selon le cas (id de l'objet)
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_catid(cls,cat_id):
        return cls.query.filter_by(id=cat_id).first()

