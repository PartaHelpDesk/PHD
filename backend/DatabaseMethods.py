import pyodbc
    
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

    def Test(self):
        cnxn = pyodbc.connect('DRIVER='+self.driver+';PORT=1433;SERVER='+self.server+';PORT=1443;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        cursor = cnxn.cursor()

        cursor.execute("SELECT * FROM users")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()

    def GetValue(self, sqlstring, params):
        #connect to DB
        cnxn = pyodbc.connect('DRIVER='+self.driver+';PORT=1433;SERVER='+self.server+';PORT=1443;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        cursor = cnxn.cursor()
        
        #If user has params use them
        if params is not None:
            cursor.execute(sqlstring, params)
        else:
            cursor.execute(sqlstring)

        result = cursor.fetchone()

        #Check if result exists
        if result is None:
            return None
        else:
            return result[0]    
      
      

    def GetDataTable(self, sqlstring, columncount):
        cnxn = pyodbc.connect('DRIVER='+self.driver+';PORT=1433;SERVER='+self.server+';PORT=1443;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        cursor = cnxn.cursor()
        
        cursor.execute(sqlstring)

        # while row:
        #     i = 0
        #     while i < columncount:
        #         output = output + ' ' + (str(row[i]))
        #         i = i + 1
        #         row = cursor.fetchone()
        #     print(output)
        #     output = ''



            

           
