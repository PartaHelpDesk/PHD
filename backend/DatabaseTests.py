import DatabaseMethods

dbm = DatabaseMethods.DatabaseMethods()

name = dbm.GetValue("SELECT username from users where FirstName = 'taylor'", None)
print(name)

result = dbm.GetDataTable("SELECT * FROM Users", None)
i = 0
while i < len(result):
    print(result[i])
    i = i + 1

