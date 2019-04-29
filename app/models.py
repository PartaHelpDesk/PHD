from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from app.initialization import login_manager
from app import DatabaseMethods as dm
#for jacob don't delete
#import DatabaseMethods as dm


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


class User(UserMixin):
    
    def __init__(self, username):
        self.level = None
        self.user_id = None
        self.username = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.is_active = False
        self.authenticated = False

        if username is not None:

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

    def SetUserInfo(self, dr):
        level = dr.GetColumnValue('Level')
        user_id = dr.GetColumnValue('UserID')
        username = dr.GetColumnValue('Username')
        first_name = dr.GetColumnValue('FirstName')
        last_name = dr.GetColumnValue('LastName')
        email = dr.GetColumnValue('Email')
        active = dr.GetColumnValue('Active')

        self.level = level
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_active = active
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
        return "%s" % (self.username)


class Tickets:

    def __init__(self):
        self.ticket_id = None
        self.title = None
        self.category = None
        self.user_id = None
        self.status = None
        self.create_dt = None
        self.close_dt = None
        self.last_update_dt = None
        self.department = None
        self.description = None
        self.username = None
        self.first_name = None
        self.last_name = None
        self.days_open = None
    
    def createTicketObject(self, dr):
        t = Tickets()
        t.ticket_id = dr.GetColumnValue('TicketID')
        t.title = dr.GetColumnValue('Title')
        t.category = dr.GetColumnValue('Category')
        t.user_id = dr.GetColumnValue('CreatedUserID')
        t.status = dr.GetColumnValue('Status')
        t.create_dt = dr.GetColumnValue('MCreateDate')
        t.close_dt = dr.GetColumnValue('ClosedDate')
        t.last_update_dt = dr.GetColumnValue('MLastUpdated')
        t.department = dr.GetColumnValue('Department')
        t.description = dr.GetColumnValue('Description')
        t.username = dr.GetColumnValue('Username')
        t.first_name = dr.GetColumnValue('FirstName')
        t.last_name = dr.GetColumnValue('LastName')
        t.days_open = dr.GetColumnValue('DaysOpen')
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
    
    @classmethod
    def getTicketFromID(cls, id):
        dbm = dm.DatabaseMethods()
        dt = dbm.GetTicketInfo(id)
        t = Tickets()
        return t.createTicketObject(dt.data_rows[0])



class TicketHistory:
    def __init__(self, ticketID):
        dbm = dm.DatabaseMethods()
        dt = dbm.GetTicketHistory(ticketID)

        self.TicketHistoryEvents = []
        for dr in dt.data_rows:
            self.TicketHistoryEvents.append(TickeHistoryEvent(dr))

class TickeHistoryEvent:
    def __init__(self, dr):
        self.Category = dr.GetColumnValue('Category')
        self.Title = dr.GetColumnValue('Title')
        self.Status = dr.GetColumnValue('Status')
        self.Department = dr.GetColumnValue('Department')
        self.Description = dr.GetColumnValue('Description')
        self.Comment = dr.GetColumnValue('Comment')
        self.Entered_By = dr.GetColumnValue('EnteredBy')
        self.Date = dr.GetColumnValue('Date')



        


        

