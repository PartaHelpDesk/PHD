
class DatabaseMethods:
    import pyodbc
    def __init__():
        self.server = 'partahelpdeskserver.database.windows.net'
        self.database = 'PartaHelpDesk'
        self.username = 'phdadmin'
        self.password = 'Capstone2019!'
        self.driver= '{ODBC Driver 13 for SQL Server}'

    def GetDataTable():
        cnxn = pyodbc.connect('DRIVER='+self.driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()

        cursor.execute("SELECT * FROM users")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()