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
        self.driver= '{ODBC Driver 17 for SQL Server}'

    def ExecuteSql(self, sqlstring, params):
         #connect to DB
        cnxn = pyodbc.connect('DRIVER='+self.driver+';PORT=1433;SERVER='+self.server+';PORT=1443;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        cursor = cnxn.cursor()
        
        #If user has params use them
        if params is not None:
            cursor.execute(sqlstring, params)
        else:
            cursor.execute(sqlstring)

        return cursor

    def Test(self):
        cnxn = pyodbc.connect('DRIVER='+self.driver+';PORT=1433;SERVER='+self.server+';PORT=1443;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        cursor = cnxn.cursor()

        cursor.execute("SELECT * FROM users")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()

    def GetValue(self, sqlstring, params):
        cursor = DatabaseMethods.ExecuteSql(self, sqlstring, params)


        result = cursor.fetchone()

        #Check if result exists
        if result is None:
            return None
        else:
            return result[0] 
        
        cursor.close()
           
      
      

    def GetDataTable(self, sqlstring, params):
        cursor = DatabaseMethods.ExecuteSql(self, sqlstring, params)

        #make a 2D array
        columns = [column[0] for column in cursor.description]


        results  = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))


        
        return results

        

        # while row:
        #     i = 0
        #     while i < columncount:
        #         output = output + ' ' + (str(row[i]))
        #         i = i + 1
        #         row = cursor.fetchone()
        #     print(output)
#     output = ''