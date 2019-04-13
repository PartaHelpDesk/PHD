from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from app.initialization import login_manager
from app import DatabaseMethods as dm


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


class User(UserMixin):
    
    def __init__(self, username):
        self.username = username
        self.authenticated = False
    
    def is_authenticated(self):
        return self.authenticated
    
    def is_active(self):
        return True

    def get_id(self):
        return self.username
    
    def is_anonymous(self):
        return False
    
    def __repr__(self):
        return "%s" % (sself.username)

class Tickets
    

