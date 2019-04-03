import pymssql


conn = pymssql.connect(server='partahelpdeskserver.database.windows.net', user='phdadmin', password='Capstone2019!', database='PartaHelpDesk', charset='UTF-8')

cu = conn.cursor()

cu.execute("select * from 仓库")
