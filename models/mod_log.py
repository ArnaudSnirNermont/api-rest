from db import db
from time import time


class LogModel(db.Model):

    #SQLAlchemy
    __tablename__ = "logs" #association avec la table de la BDD
    #Détail des colonnes
    id = db.Column(db.Integer, primary_key= True)
    msg = db.Column(db.String(150))
    timestamp = db.Column(db.String(50))
    user = db.Column(db.String(80))
    id_categorie = db.Column(db.Integer, db.ForeignKey("categories.id"))
    #Récupération de la catégorie du log dans une propriété categorie grâce
    #à la relatin
    categorie = db.relationship("CategorieModel")

    def __init__(self,msg,user, id_categorie) -> None:
        self.msg = msg
        self.timestamp = str(time())
        self.user = user
        self.id_categorie = id_categorie

    def json(self):
        #contruit une représentation json de l'objet log
        #Grâce à la relation, on peut accéder à l'enregistrement de la catégorie du log pour 
        #lequel on accède à l'attribut nom_cat
        return {"id":self.id, "msg":self.msg,"user": self.user, "date/heure": \
            self.timestamp, "catégorie" : self.categorie.nom_cat}
        
    def save_to_db(self) :
        #Insertion ou update selon le cas (id de l'objet)
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_logid(cls,logid):
        #Equivalent à une requête SQL SELECT * from logs WHERE logs.id=logid LIMIT 1
        return cls.query.filter_by(id=logid).first()

