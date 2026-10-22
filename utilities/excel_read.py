import openpyxl


class NewExcelReader:

    def read_excel_cell(self, row_no, col_no):
        book = openpyxl.load_workbook('C:\\Users\\annma\\Downloads\\python Data_Login.xlxs')
        sheet = book["login_data"]
        return sheet.cell(row=row_no, column=col_no).value