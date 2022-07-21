import openpyxl

class Data_Transform:
    def __init__(self, param, row):
        self.param = param
        self.row = row
    def calculation(self):
        #тут вычисление новых значений
    def read_param(self):
        f = openpyxl.load_workbook("datagrafiks2.xlsx")
        sheet = f["Первый лист"]
        i = 1
        for key in self.param:
            self.param[key] = sheet.cell(row = self.row, column = i).value()
            i += 1
        f.save("datagrafiks2.xlsx")
    def write_param(self):
        f = openpyxl.load_workbook("datagrafiks2.xlsx")
        sheet = f["Первый лист"]
        i = 1
        for key in self.param:
            sheet.cell(row=self.row, column=i, value=self.param[key])
            i += 1
        f.save("datagrafiks2.xlsx")
    def removing_param(self):
        f = openpyxl.load_workbook("datagrafiks2.xlsx")
        sheet = f["Первый лист"]
        for i in range(1, 15):
            sheet.cell(row=self.row, column=i, value="")
        f.save("datagrafiks2.xlsx")
        self.param.clear()