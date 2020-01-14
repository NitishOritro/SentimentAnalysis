import xlrd


# Function definition is here

def LoadData(dataParameter):

    with open(dataParameter, encoding="utf8") as myfile:
        data = myfile.read()
    myfile.close()

    sentence = ""
    listOfWord = []
    fullStop = "।"
    newLine = "\n"

    res = None
    for i in range(0, len(data)):
        if data[i] != fullStop:
            if data[i] == newLine:
                res = i
                listOfWord.append(sentence)
                sentence = ""
            else:
                sentence = sentence + data[i]
        else:
            break

    return listOfWord

# Function definition is here
def LoadPositiveNegativeData(listOfPositiveWord, listOfNegativeWord, findWord):

    score = 0
    count = 0
    # find a word
    #find = findWord
    flag = ""
    for i in range(0, len(listOfPositiveWord)):
        if listOfPositiveWord[i] == findWord:
            flag = "true"
            score = 1
            print("++++++ Word: "+findWord)
            break
        else:
            flag = "N/F"
    if flag == "N/F":
        for i in range(0, len(listOfNegativeWord)):
            if listOfNegativeWord[i] == findWord:
                flag = "true"
                score = -1
                print("------- Word: "+ findWord)
                break
            else:
                flag = "N/F"

    if flag == "N/F":
        score = -999

    return score


def CountNegativeData(listOfNegWord, findWord):

    count = 0
    flag = ""

    for i in range(0, len(listOfNegWord)):
        if listOfNegWord[i] == findWord:
            flag = "True"
            count = count+1
            #print("-Counted Negative - Word: " + str(count))
            break
        else:
            flag = "N/F"

    return flag

# Function definition is here
def LoadExcle(dataParameter):
    wb = xlrd.open_workbook(dataParameter)
    sheet = wb.sheet_by_index(0)

    sheet.cell_value(0, 0)

    listOfWord = [()]
    dataValue = 0
    for i in range(sheet.nrows):
        data = sheet.cell_value(i, 0)
        dataValue = sheet.cell_value(i, 1)
        #append(tuple([3, 4]))
        listOfWord.append(tuple([data, dataValue]))
        # for j in range(0, len(data)):

    #print(listOfWord)

    return listOfWord


def cCDcCSData(listOfcCDcCSWord, findWord):
    flag = ""
    wb = xlrd.open_workbook("data/CCD-CCS/CCID.xlsx")
    sheet = wb.sheet_by_index(0)
    value = 0
    index = 0
    for i in range(0, len(listOfcCDcCSWord)):
        if i !=0 and listOfcCDcCSWord[i][0] == findWord:
            flag = "True"

            value = listOfcCDcCSWord[i][1]
            print("CCD-CCS word:" + findWord+ " and Value is: "+ str(value))
            break
        else:
            flag = "N/F"
            value = 1

    return value

def JJJQData(listOfcCDcCSWord, findWord):
    flag = ""

    value = 0
    index = 0
    for i in range(0, len(listOfcCDcCSWord)):
        if i !=0 and listOfcCDcCSWord[i][0] == findWord:
            #index = i
            flag = "True"
            value = listOfcCDcCSWord[i][1]
            print("JJ-JQ word:"+findWord +" and Value is: "+ str(value))

            break
        else:
            flag = "N/F"
            value = 1

    return value