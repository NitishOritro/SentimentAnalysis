# Program to extract a particular row value
import xlrd
import functionPython

dataParameter = "data/CCD-CCS/CCID.xlsx"
listOfcCDcCSWord = functionPython.LoadExcle(dataParameter)
dataParameter = "data/Adjective-Adverb/exel/jj-jq.xlsx"
listOfJJJQCSWord = functionPython.LoadExcle(dataParameter)

dataParameter = "data/negative-word/neg.txt"
listOfNegWord = functionPython.LoadData(dataParameter)


count = 0
flag = ""

for i in range(0, len(listOfNegWord)):
    if listOfNegWord[i] == "নয়":
        flag = "True"
        count = count+1
        #print("-Counted Negative - Word: " + str(count))
        break
    else:
        flag = "N/F"

print(flag)

#score = functionPython.JJJQData(listOfJJJQCSWord, "অল্প")


#print(score)
























"""
#loc = ("data/CCD-CCS/CCID.xlsx")
loc = ("data/CCD-CCS/CCID.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

print(sheet.cell_value(0, 1))

listOfSentence = []

for i in range(sheet.nrows):
    data = sheet.cell_value(i, 0)
    listOfSentence.append(data)
    #for j in range(0, len(data)):



print(listOfSentence)

search = "পুনশ্চ"

for i in range(sheet.nrows):
    if search == sheet.cell_value(i, 0):
        datavalue = sheet.cell_value(i, 1)
        print(datavalue)
        break




"""
#print(sheet.row_values(1))

