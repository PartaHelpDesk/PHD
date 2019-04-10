from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from flask.ext.login import login_user, logout_user



class User(UserMixin):
    
    def __init__(self, id, username):
        self.id = id
        self.username = username
        

    def get_id(self):
        return self.id
    
    def __repr__(self):
        return "%d/%s" % (self.id, self.username)
    

@login_manager.user_loader
def load_user(user_id):
    return User(user_id, username)
