import DatabaseMethods

dbm = DatabaseMethods.DatabaseMethods()

#dbm.Test()

name = dbm.GetValue("SELECT username from users where FirstName = 'taylr'", None)
print(name)
#dbm.GetDataTable("Select * from users", 4)