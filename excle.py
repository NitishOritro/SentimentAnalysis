# Program to extract a particular row value
import xlrd

loc = ("data/CCD-CCS/CCID.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

listOfSentence = []

for i in range(sheet.nrows):
    data = sheet.cell_value(i, 0)
    listOfSentence.append(data)
    #for j in range(0, len(data)):



print(listOfSentence)


""""
for i in range(sheet.nrows):
    if search == sheet.cell_value(i, 0):
        print(sheet.cell_value(i, 1))


print(sheet.row_values(1))
"""
