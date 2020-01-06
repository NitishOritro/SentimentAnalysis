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
            count = count +1
            print("-Counted Negative - Word: " + str(count))
            break
        else:
            flag = "N/F"

    return flag


