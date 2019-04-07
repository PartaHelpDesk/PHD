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
        #Will exectue sql if not return_value

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

        #Create a 2D array
        columns = [column[0] for column in cursor.description]

        #Add db restults
        results  = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        
        #Check if result exists
        if not results:
            results = None

        cursor.close()
        return results


    def GetITEmails(self):
        sql = "SELECT Email from Users WHERE [Level] in (2,3)"
        return DatabaseMethods.GetDataTable(self, sql, None)

    def GetUserAccountInfo(self, user_id):
        sql = "SELECT * FROM Users WHERE UserID = ?"
        return DatabaseMethods.GetDataTable(self, sql, user_id)
    
    def CreateTicket(self, title, category, user, status, department, location, description):
        sql = "INSERT INTO Tickets (Title, Category, CreatedUserID, [Status], Department, [Location], [Description]) "
        sql = sql + "VALUES ( ?, ?, ?, ?, ?, ?, ?) "
        DatabaseMethods.ExecuteSql(self, sql, (title, category, user, status, department, location, description),False)
    
    # def UpdateTicket(self, title, category, user, status, department, location, description):
    #     #Get current ticket info
    #     sql = "SELECT * FROM Tickets "
    #     sql = "UPDATE Tickets"
        