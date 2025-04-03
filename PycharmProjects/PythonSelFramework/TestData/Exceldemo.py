import openpyxl
book = openpyxl.load_workbook("/Users/idasaravanan/Library/Containers/com.microsoft.Excel/Data/Desktop/PythonDemo.xlsx")

sheet = book.active
cell = sheet.cell(row=1, column=2)
print(cell.value)
