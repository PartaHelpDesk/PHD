import pymssql


conn = pymssql.connect(server='partahelpdeskserver.database.windows.net', user='phdadmin@partahelpdeskserver', password='Capstone2019!', database='PartaHelpDesk')

cu = conn.cursor()

cu.execute("select * from 仓库")
