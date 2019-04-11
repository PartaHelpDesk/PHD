
import pyodbc ,Datatable, DataRow #DEBUG

#from backend import Datatable #SERVER
#from backend import DataRow #SERVER

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
        #self.driver= '{ODBC Driver 17 for SQL Server}'


    def ExecuteSql(self, sqlstring, params, return_value):
        #Will return a value if return_value
        #Will execute sql if not return_value

        cnxn = pyodbc.connect('DRIVER='+self.driver+';PORT=1433;SERVER='+self.server+';PORT=1443;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        cursor = cnxn.cursor()

        #If user has params use them
        if params is not None:
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
            
            for i in range(column_count):
                #parse the row's columns
                dr.AppendValue(column_names[i], str(row[i]))

            dt.AddRow(dr)

        cursor.close()
        return dt

    def GetITEmails(self):
        sql = "SELECT Email from Users WHERE [Level] in (2,3)"
        dt = DatabaseMethods.GetDataTable(self, sql, None)
        index = 0
        list_of_emails = []
        while index != dt.get_Size():
            dr = dt.GetRow(index)
            list_of_emails.append(dr.GetColumnValue("Email"))
            index += 1
        return list_of_emails

    def GetUserID(self, user_name):
        sql = "SELECT UserID FROM USERS WHERE Username = ?"
        id = DatabaseMethods.GetValue(self, sql, user_name)
        return int(id)

    def GetUserAccountInfo(self, user_id):
        #Gets all user info
        sql = "SELECT * FROM Users WHERE UserID = ?"
        return DatabaseMethods.GetDataTable(self, sql, user_id)

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
        sql = sql + "VALUES ( ?, ?, ?, ?, ?, ?) "
        DatabaseMethods.ExecuteSql(self, sql, (title, category, user_id, status, department, description),False)

    def UpdateTicket(self, user_id, ticket_id, title, category, status, department, description):
        update_title = None
        update_category = None
        update_status = None
        update_department = None
        update_description = None

        #Get current ticket info
        sql = "SELECT * FROM Tickets WHERE TicketID = ?"

        dt = DatabaseMethods.GetDataTable(self, sql, (ticket_id))
        dr = dt.GetRow(0)

        old_title = dr.GetColumnValue("Title")
        old_category = dr.GetColumnValue("Category")
        old_status = dr.GetColumnValue("Status")
        old_department = dr.GetColumnValue("Department")
        old_description = dr.GetColumnValue("Description")

        #Compare old vs new, if changes save
        change_made = False

        if old_title != title:
            update_title = title
            change_made = True

        if old_category != category:
            update_category = category
            change_made = True
        
        if old_status != status:
            update_status = status
            change_made = True    

        if old_department != department:
            update_department = department
            change_made = True

        if old_description != description:
            update_description = description
            change_made = True


        if change_made:
            #update ticket
            sql = "UPDATE Tickets "
            sql = sql + " SET Title = ?, Category = ?, [Status] = ?, Department = ?, [Description] = ? "
            sql = sql + " WHERE TicketID = ?"
            
            DatabaseMethods.ExecuteSql(self, sql, (title, category, status, department, description, ticket_id), False)


            #update ticket history
            sql = "INSERT INTO TicketHistory (TicketID, Title, Category, [Status], Department, [Description], UserID)"
            sql = sql + "VALUES ( ?, ?, ?, ?, ?, ?, ?)"
            
            DatabaseMethods.ExecuteSql(self, sql, (ticket_id, update_title, update_category, update_status, update_department, update_description ,user_id), False)
    
