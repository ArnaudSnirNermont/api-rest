from models.mod_user import UserModel
import hmac

def authentification (username, password):
    #user = userid_mapping[username]
    user = UserModel.find_by_username(username)
    #user = username_mapping.get(username, None) #Intérêt de get : valeur par défaut
    #if user is not None and user.password==password:
    if user is not None and hmac.compare_digest(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)
    #return userid_mapping.get(user_id,None)