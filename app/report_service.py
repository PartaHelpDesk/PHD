import matplotlib.pyplot as plt
from app import DatabaseMethods, Datatable, DataRow
from array import *

def report_by_category():
    dbm = DatabaseMethods.DatabaseMethods()
    sql = "SELECT DISTINCT Category, COUNT( Category ) AS Count "
    sql = sql + "FROM Tickets "
    sql = sql + "GROUP BY Category"

    reportTable = dbm.GetDataTable(sql, None)

    #reportTable.PrintValues()

    slices_hours = []
    activities = []
    index = 0
    while index != reportTable.get_Size():
                dr = reportTable.GetRow(index)
                slices_hours.append(dr.GetColumnValue("Count"))
                index += 1
    #print(slices_hours)
    index = 0
    while index != reportTable.get_Size():
                dr = reportTable.GetRow(index)
                activities.append(dr.GetColumnValue("Category"))
                index += 1
    #print(activities)
    #activities = ['Hardware', 'Internet', 'Login','Network','Phone Server', 'Printer']
    colors = ['r', 'g','b','y','k','m']
    plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
    #plt.show()
    plt.savefig('app/static/images/example_category_report.png')


def report_by_department():
    dbm = DatabaseMethods.DatabaseMethods()
    sql = "SELECT DISTINCT Department, COUNT( Department ) AS Count "
    sql = sql + "FROM Tickets "
    sql = sql + "GROUP BY Department"

    reportTable = dbm.GetDataTable(sql, None)

    #reportTable.PrintValues()

    slices_hours = []
    activities = []
    index = 0
    while index != reportTable.get_Size():
                dr = reportTable.GetRow(index)
                slices_hours.append(dr.GetColumnValue("Count"))
                index += 1
    #print(slices_hours)
    index = 0
    while index != reportTable.get_Size():
                dr = reportTable.GetRow(index)
                activities.append(dr.GetColumnValue("Department"))
                index += 1
    #print(activities)
    #activities = ['Hardware', 'Internet', 'Login','Network','Phone Server', 'Printer']
    colors = ['r', 'g','b','y','k','m']
    plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
    #plt.show()
    plt.savefig('app/static/images/example_department_report.png')

