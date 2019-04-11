import pymssql
server = 'partahelpdeskserver.database.windows.net'
database = 'PartaHelpDesk'
username = 'phdadmin'
password = 'Capstone2019!'
driver= '{ODBC Driver 13 for SQL Server}'

cnxn = pymssql.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT username, email FROM users")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()