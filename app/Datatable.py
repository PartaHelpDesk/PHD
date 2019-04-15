
class DataTable:


    def __init__(self):
        self.data_rows = []
        self.IsEmpty = True
    
    def __nonzero__(self):
        return self.IsEmpty

    def PrintValues(self):
        if self.data_rows is None:
            print('empty') 
        for row in self.data_rows:
            row.PrintRow()

    def AddRow(self, data_row):
        self.data_rows.append(data_row)
        self.IsEmpty = False

    def GetRow(self, index):
        return self.data_rows[index]

    def get_Size(self):
        return len(self.data_rows)
      
