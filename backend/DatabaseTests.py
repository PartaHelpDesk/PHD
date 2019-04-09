import DatabaseMethods, Datatable, DataRow

dbm = DatabaseMethods.DatabaseMethods()

# name = dbm.GetValue("SELECT username from users where FirstName = 'taylor'", None)
# print(name)


# result = dbm.GetDataTable("SELECT * FROM Users", None)
# i = 0
# while i < len(result):
#     print(result[i])
#     i = i + 1

# if not dbm.GetUserAccountInfo(1):
#     print("Hey")

# dbm.CreateTicket('Title',1,2,65,2,0,'A REALLY LONG MESSAGE HERE BECUASE ITS  A TICKET')

#dt = Datatable.DataTable()

#dt = dbm.GetITEmails()
#dt.PrintValues()

#index = 0
list_of_emails = []
#while index != dt.get_Size():
    #dr = dt.GetRow(index)
    #list_of_emails.append(dr.GetColumnValue("Email"))
    #index += 1

list_of_emails = dbm.GetITEmails()

print(list_of_emails)

#print(results)

# dt.SetDataTable(results)

#value = dbm.GetValue("SELECT Password FROM Users WHERE Username = ?" , ('tnaungay'))
#print (value)

#dr = dt.GetRow(0)
#print(dr.GetColumnValue("Description"))

# dt.PrintValues()


        
# dbm.UpdateTicket(34,1, "Title Change", 2,  1, 2, 3, "New descript")