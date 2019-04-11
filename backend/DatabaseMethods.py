import pyodbc ,Datatable, DataRow #DEBUG
# from backend import Datatable #SERVER
# from backend import DataRow #SERVER
import pyodbc
from array import *

class DatabaseMethods:
    server = ''
    database = ''
    username = ''
    password = ''
    driver = ''

    def __init__(self):
        self.server = 'partahelpdeskserver.database.windows.net'
        self.database = 'PartaHelpDesk'
        self.username = 'phdadmin'
        self.password = 'Capstone2019!'
        self.driver= '{ODBC Driver 13 for SQL Server}'

    def ExecuteSql(self, sqlstring, params, return_value):
        #Will return a value if return_value
        #Will execute sql if not return_value

        cnxn = pyodbc.connect('DRIVER='+self.driver+';PORT=1433;SERVER='+self.server+';PORT=1443;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        cursor = cnxn.cursor()

        #If user has params use them
        if params is not None:
            print(params)
            cursor.execute(sqlstring, params)
        else:
            cursor.execute(sqlstring)

        if return_value:
            return cursor
        else:
            cnxn.commit()


    def GetValue(self, sqlstring, params):
        cursor = DatabaseMethods.ExecuteSql(self, sqlstring, params, True)
        result = cursor.fetchone()

        cursor.close()

        #Check if result exists
        if result is None:
            return None
        else:
            return result[0]


    def GetDataTable(self, sqlstring, params):
        cursor = DatabaseMethods.ExecuteSql(self, sqlstring, params, True)

        column_names = [column[0] for column in cursor.description]
        column_count = len(column_names)

        dt = Datatable.DataTable()

        for row in cursor.fetchall():
            #create new dr to add
            dr = DataRow.DataRow()

            for i in (0, column_count - 1):
                #parse the row's columns
                dr.AppendValue(column_names[i], row[i])

            dt.AddRow(dr)

        cursor.close()
        return dt

    def GetITEmails(self):
        sql = "SELECT Email from Users WHERE [Level] in (2,3)"
        return DatabaseMethods.GetDataTable(self, sql, None)

    def GetUserID(self, user_name):
        sql = "SELECT UserID FROM USERS WHERE Username = ?"
        id = DatabaseMethods.GetValue(self, sql, user_name)
        return int(id)

    def GetUserAccountInfo(self, user_id):
        #Gets all user info
        sql = "SELECT * FROM Users WHERE UserID = ?"
        return DatabaseMethods.GetDataTable(self, sql, user_id)

<<<<<<< HEAD
    def CreateTicket(self, title, category, user_id, status, department, location, description):
        sql = "INSERT INTO Tickets (Title, Category, CreatedUserID, [Status], Department, [Location], [Description]) "
=======
    def GetTicketInfo(self, ticket_id):
        #Gets ticket infor for one ticket
        sql = "SELECT * FROM Tickets WHERE TicketID = ?"
        return DatabaseMethods.GetDataTable(self, sql, ticket_id)

    def GetAllActiveTickets(self):
        #Gets all active tickets
        sql = "SELECT * FROM Tickets WHERE [Status] <> 'Closed'"
        return DatabaseMethods.GetDataTable(self, sql, None)

    def CreateTicket(self, title, category, user_id, status, department, description):
        #Creates a ticket
        sql = "INSERT INTO Tickets (Title, Category, CreatedUserID, [Status], Department, [Description]) "
>>>>>>> master
        sql = sql + "VALUES ( ?, ?, ?, ?, ?, ?, ?) "
        DatabaseMethods.ExecuteSql(self, sql, (title, category, user_id, status, department, location, description),False)

    def UpdateTicket(self, user_id, ticket_id, title, category, status, department, location, description):
        #Get current ticket info
        sql = "SELECT * FROM Tickets WHERE TicketID = ?"
<<<<<<< HEAD
        results = DatabaseMethods.GetDataTable(self, sql, (ticket_id))
=======

        dt = DatabaseMethods.GetDataTable(self, sql, (ticket_id))
        dr = dt.GetRow(0)

        sql = "INSERT INTO"
>>>>>>> master

    
