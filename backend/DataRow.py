class DataRow:
    columns = []
    values = []

    def __init__(self):
        self.columns = []
        self.values = []

    def PrintRow(self):
        for i in range(0,len(self.columns)): 
            #convert non string values into string
            print(self.columns[i] + "-" + str(self.values[i]))
        print("------------------------")

    def AppendValue(self, column, value):
        self.columns.append(column)
        self.values.append(value)

    def GetColumnValue(self, column_name):
        index = self.columns.index(column_name)
        return self.values[index]

    def Clear(self):
        self.columns = []
        self.values = []

    


        