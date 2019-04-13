#from backend import DataRow
from app import DataRow

class DataTable:
    data_rows = [] #Will be of type DatabaseMethods.DataRow

    def __init__(self):
        self.data_rows = []

    def PrintValues(self):
        if self.data_rows is None:
            print('empty') 
        for row in self.data_rows:
            row.PrintRow()

    def AddRow(self, data_row):
        self.data_rows.append(data_row)

    def GetRow(self, index):
        return self.data_rows[index]

    def IsEmpty(self):
        if len(self.data_rows) == 0:
            return True
        return False

    def get_Size(self):
        return len(self.data_rows)
      
