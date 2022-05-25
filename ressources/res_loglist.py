from flask_restful import Resource
from models.mod_log import LogModel

class ResLogList(Resource):
    def get(self):
        return {'logs' : [log.json() for log in LogModel.query.all()]}
        #return {'logs' : list(map(lambda x : x.json(),LogModel.query.all()))}