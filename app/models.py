from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from app.initialization import login_manager
from app import DatabaseMethods as dm


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


class User(UserMixin):
    
    def __init__(self, username):
        dbm = dm.DatabaseMethods()
        dt = dbm.GetUserAccountInfo(username)
        dr = dt.GetRow(0)

        level = dr.GetColumnValue('Level')
        user_id = dr.GetColumnValue('UserID')
        first_name = dr.GetColumnValue('FirstName')
        last_name = dr.GetColumnValue('LastName')
        email = dr.GetColumnValue('Email')

        self.level = level
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_active = True
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



class Tickets:

    def __init__(self):
        self.ticket_id = None
        self.title = None
        self.category = None
        self.user_id = None
        self.status = None
        self.create_dt = None
        self.close_dt = None
        self.department = None
        self.description = None

    def createTicketObject(self, dr):
        t = Tickets()
        t.ticket_id = dr.GetColumnValue('TicketID')
        t.title = dr.GetColumnValue('Title')
        t.category = dr.GetColumnValue('Category')
        t.user_id = dr.GetColumnValue('CreatedUserID')
        t.status = dr.GetColumnValue('Status')
        t.create_dt = dr.GetColumnValue('CreateDate')
        t.close_dt = dr.GetColumnValue('ClosedDate')
        t.department = dr.GetColumnValue('Department')
        t.description = dr.GetColumnValue('Description')
        return t
    
    def getAllUserTicket(self, user_id):
        dbm = dm.DatabaseMethods()
        data_tbl = dbm.GetAllUserTickets(user_id)
        queue = []
        for i in data_tbl.data_rows:
            queue.append(self.createTicketObject(i))
        return queue

    def getTicketQueue(self):
        dbm = dm.DatabaseMethods()
        data_tbl = dbm.GetAllActiveTickets()
        queue = []
        for i in data_tbl.data_rows:
            queue.append(self.createTicketObject(i))
        return queue
        


        

