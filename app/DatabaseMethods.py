
from app import Datatable, DataRow #DEBUG
#import Datatable, DataRow
from app.models import User
from app import email_service

import pyodbc
from werkzeug.security import generate_password_hash, check_password_hash

class DatabaseMethods:

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
    
        if params != None:
            cursor.execute(sqlstring, params)
        else:
            cursor.execute(sqlstring)
        
        if return_value:
            return cursor
        else:
            cnxn.commit()


    def GetValue(self, sqlstring, params):
        cursor = self.ExecuteSql( sqlstring, params, True)
        result = cursor.fetchone()

        cursor.close()

        #Check if result exists
        if result is None:
            return None
        else:
            return result[0]


    def GetDataTable(self, sqlstring, params):
        cursor = self.ExecuteSql( sqlstring, params, True)

        column_names = [column[0] for column in cursor.description]
        column_count = len(column_names)

        dt = Datatable.DataTable()
        dt.IsEmpty = True

        for row in cursor.fetchall():
            #create new dr to add
            dr = DataRow.DataRow()
            
            for i in range(column_count):
                #parse the row's columns
                dr.AppendValue(column_names[i], str(row[i]))
                dt.IsEmpty = False

            dt.AddRow(dr)

        cursor.close()
        return dt

    def GetITEmails(self):
        #Gets all emails from IT and admin accounts
        sql = "SELECT Email from Users WHERE [Level] in (2,3)"
        dt = self.GetDataTable( sql, None)
        list_of_emails = []
        for dr in dt.data_rows:
            list_of_emails.append(dr.GetColumnValue("Email"))
        return list_of_emails

    def GetUsername(self, user_id):
        sql = "SELECT Username FROM USERS WHERE UserID = ?"
        user_name = self.GetValue(sql, user_id)
        return user_name

    def GetUserID(self, user_name):
        sql = "SELECT UserID FROM USERS WHERE Username = ?"
        id = self.GetValue(sql, user_name)
        return id

    def GetUserAccountInfo(self, username):
        #Gets all user info
        sql = "SELECT * FROM Users WHERE Username = ?"
        return self.GetDataTable(sql, username)

    def CheckUserPassword(self, username, password):
        #Get hashed user pw
        sql = "SELECT Password FROM Users WHERE Username = ?"
        db_password = self.GetValue(sql, username)

        #Hash what users entered

        #compare
        if check_password_hash(db_password, password):
            return True
        else:
            return False

    def GetAllUsers(self, active):
        sql = "SELECT * FROM Users WHERE Active = ?"
        dt = self.GetDataTable(sql, active)
        
        users = []
        for dr in dt.data_rows:
            user = User(None)
            user.SetUserInfo(dr)
            users.append(user)

        return users

    def HashPassword(self, password):
        return generate_password_hash(password)

    def GetTicketInfo(self, ticket_id):
        #Gets ticket infor for one ticket
        sql = "SELECT t.*, u.Username, u.FirstName, u.LastName, \
        DATEDIFF(DAY, t.CreateDate, GETDATE()) as DaysOpen FROM Tickets t"
        sql = sql + ' JOIN Users u ON t.CreatedUserID = u.UserID '
        sql = sql + ' WHERE TicketID = ?'
        return self.GetDataTable(sql, ticket_id)

    def GetAllActiveTickets(self):
        #Gets all active tickets (admin/IT)
        sql = "SELECT t.*, u.Username, u.FirstName, u.LastName, \
        DATEDIFF(DAY, t.CreateDate, GETDATE()) as DaysOpen FROM Tickets t"
        sql = sql + ' JOIN Users u ON t.CreatedUserID = u.UserID '
        sql = sql + " WHERE [Status] <> 'Closed'"
        return self.GetDataTable(sql, None)

    def GetAllUserTickets(self, user_id):
        #Dashboard Tickets related to user
        sql = "SELECT t.*, u.Username, u.FirstName, u.LastName, \
        DATEDIFF(DAY, t.CreateDate, GETDATE()) as DaysOpen FROM Tickets t"
        sql = sql + ' JOIN Users u ON t.CreatedUserID = u.UserID '
        sql = sql + " WHERE t.CreatedUserID = ? AND t.Status <> 'Closed'" 
        return self.GetDataTable(sql, user_id)

    def GetTicketFiltered(self, filter_text):
        sql = "SELECT t.*, u.Username, u.FirstName, u.LastName, \
        DATEDIFF(DAY, t.CreateDate, GETDATE()) as DaysOpen FROM Tickets t "
        sql = sql + ' JOIN Users u ON t.CreatedUserID = u.UserID '

        if not filter_text is None:
            sql = sql + ' WHERE t.Title LIKE ? OR t.Category LIKE ? OR t.[Status] LIKE ? OR t.Department LIKE ? OR t.[Description] LIKE ? OR '
            sql = sql + ' u.UserName LIKE ? OR u.FirstName LIKE ? OR u.LastName LIKE ? '
            filter_text = '%' + filter_text + '%' #add wildcards
            return self.GetDataTable(sql, (filter_text,filter_text,filter_text,filter_text,filter_text,filter_text,filter_text,filter_text))
        else:
            return self.GetDataTable(sql, None)

    def CreateTicket(self, title, category, user_id, status, department, description):
        #Creates a ticket
        sql = "INSERT INTO Tickets (Title, Category, CreatedUserID, [Status], Department, [Description]) "
        sql = sql + "VALUES ( ?, ?, ?, ?, ?, ?) "
        self.ExecuteSql(sql, (title, category, user_id, status, department, description),False)

    def UpdateTicket(self, user_id, ticket_id, title, category, status, department, description, comment):
            #Updates the ticket in ticket table and updates ticket history
            update_title = None
            update_category = None
            update_status = None
            update_department = None
            update_description = None

            #Get current ticket info
            sql = "SELECT * FROM Tickets WHERE TicketID = ?"

            dt = self.GetDataTable(sql, (ticket_id))
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

            if comment is not None:
                change_made = True

            if change_made:
                #update ticket
                sql = "UPDATE Tickets "
                sql = sql + " SET Title = ?, Category = ?, [Status] = ?, Department = ?, [Description] = ?, LastUpdated = GETDATE() "
                sql = sql + " WHERE TicketID = ?"
                
                self.ExecuteSql(sql, (title, category, status, department, description, ticket_id), False)


                #update ticket history
                sql = "INSERT INTO TicketHistory (TicketID, Title, Category, [Status], Department, [Description], UserID, Comment)"
                sql = sql + "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)"
                
                self.ExecuteSql(sql, (ticket_id, update_title, update_category, update_status, update_department, update_description ,user_id, comment), False)

    def CreateUserAccount(self, username, level, first_name, last_name, email):
        result = self.CheckIfUserNameEmailExists(username,email, None)

        if result != '':
            return result

        #if username or email is not already in use, add to DB

        #Generate number for middle
        sql = "SELECT MAX(UserID) + 1 FROM Users"
        number = self.GetValue(sql, None)

        active = 1
        authenticated = False

        user_password = last_name + str(number) + first_name
        password = generate_password_hash(user_password)
        
        recip = []
        recip.append(email)
        emailMessage = "Your PHD Account has been created:\nUsername: " + username + "\nPassword: " + user_password
        email_service.send_email("PHD Account Created", "partahelpdesk@gmail.com", recip,emailMessage, None)

        sql =  'INSERT INTO [dbo].[Users](Username, [Level], FirstName, LastName, Email, \
            [Password], Active, [Authenticated])'
        sql += 'VALUES(?, ?, ?, ?, ?, ?, ?, ?)'

        params = (username, level, first_name, last_name, email, password, active, authenticated)
        self.ExecuteSql(sql, params, False)
        return 'Success'

    def UpdateUserAccount(self, user_id, username, level, first_name, last_name, email):
        result = self.CheckIfUserNameEmailExists(username,email, user_id)

        if result != '':
            return result
            
        sql = 'UPDATE Users  \
        SET Username = ?, Level = ?, FirstName = ?, LastName = ?, Email =? \
        WHERE UserId = ?'

        params = (username, level, first_name, last_name, email, user_id)
        self.ExecuteSql(sql, params, False)
        return 'Success'

    def CheckIfUserNameEmailExists(self, user_name, email, user_id):
        dt = None
        result = ''
        sql = 'SELECT Username, Email FROM Users WHERE (Username like ? OR Email like ?) '
        if user_id is not None:
            sql = sql + ' AND UserID <> ?'
            dt = self.GetDataTable(sql, (user_name, email, user_id))
        else:
            dt = self.GetDataTable(sql, (user_name, email))
    
        if not dt.IsEmpty:
            dr = dt.GetRow(0)
            if dr.GetColumnValue('Username').lower() == user_name.lower():
                return 'Username already exists!'
            elif dr.GetColumnValue('Email').lower() == email.lower():
                return 'Email is already in use!'
            return 'An error has occured'
        
        return result


    def GetCategories(self):
        sql = "SELECT * FROM Categories"
        return self.GetDataTable(sql, None)

    def GetDepartments(self):
        sql = "SELECT * FROM Departments"
        return self.GetDataTable(sql, None)

    def GetStatuses(self):
        sql = "SELECT * FROM Status"
        return self.GetDataTable(sql, None)

    def UpdateUserPassword(self, accountName, newpassword):
        sql = "Update users \
            SET [Password] = ? \
            WHERE Username = ?"

        HashedPassword = generate_password_hash(newpassword)
        self.ExecuteSql(sql, (HashedPassword,accountName), False)
