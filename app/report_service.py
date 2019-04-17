import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from app import DatabaseMethods, Datatable, DataRow
from array import *
from datetime import datetime
import os

def report_by_category():
    dir_name = "/Users/macbook/Documents/GitHub/PHD/app/static/images"
    test = os.listdir(dir_name)
    for item in test:
        if item.startswith('example'):
            os.remove(os.path.join(dir_name, item))

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
    colors = ['b', 'g','r','c','m','y']
    plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
    #plt.show()
    dt = datetime.now()
    dateStr = str(dt.day) + str(dt.hour) + str(dt.minute) 
    fileSavePath = 'app/static/images/example_category_report' + dateStr + '.png'
    plt.savefig(fileSavePath)
    fileSavePath = fileSavePath[len('app/'):]
    return fileSavePath


def report_by_department():
    dir_name = "/Users/macbook/Documents/GitHub/PHD/app/static/images"
    test = os.listdir(dir_name)
    for item in test:
        if item.startswith('example'):
            os.remove(os.path.join(dir_name, item))

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
    colors = ['b', 'g','r','c','m','y']
    plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
    #plt.show()
    dt = datetime.now()
    dateStr = str(dt.day) + str(dt.hour) + str(dt.minute) 
    fileSavePath = 'app/static/images/example_department_report' + dateStr + '.png'
    plt.savefig(fileSavePath)
    fileSavePath = fileSavePath[len('app/'):]
    return fileSavePath
