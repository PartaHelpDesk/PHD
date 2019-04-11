import matplotlib.pyplot as plt
import DatabaseMethods, Datatable, DataRow
from array import *

dbm = DatabaseMethods.DatabaseMethods()

sql = "SELECT DISTINCT Category, COUNT( Category ) AS Count "
sql = sql + "FROM Tickets "
sql = sql + "GROUP BY Category"

reportTable = dbm.GetDataTable(sql, None)

reportTable.PrintValues()

slices_hours = []
activities = []
index = 0
while index != reportTable.get_Size():
            dr = reportTable.GetRow(index)
            slices_hours.append(dr.GetColumnValue("Count"))
            index += 1
print(slices_hours)
index = 0
while index != reportTable.get_Size():
            dr = reportTable.GetRow(index)
            activities.append(dr.GetColumnValue("Category"))
            index += 1
print(activities)
#activities = ['Hardware', 'Internet', 'Login','Network','Phone Server', 'Printer']
colors = ['r', 'g','b','y','k','m']
plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
#plt.show()
plt.savefig('example_report.png')

emails = []
emails = dbm.GetITEmails()
print(emails)
