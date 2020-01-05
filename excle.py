# Program to extract a particular row value
import xlrd

loc = ("data/main-data/Restaurant.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

search = "অধিক"


for i in range(sheet.nrows):
    if search == sheet.cell_value(i, 0):
        print(sheet.cell_value(i, 1))


print(sheet.row_values(1))