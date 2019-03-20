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

    def GetDataTable(self):
        cnxn = pyodbc.connect('DRIVER='+self.driver+';PORT=1433;SERVER='+self.server+';PORT=1443;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        cursor = cnxn.cursor()
        print("hey")

        cursor.execute("SELECT * FROM users")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()