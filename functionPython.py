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
def LoadPositiveData(listOfPositiveWord, listOfNegativeWord, findWord):

    score = 0
    # find a word
    #find = findWord
    flag = ""
    for i in range(0, len(listOfPositiveWord)):
        if listOfPositiveWord[i] == findWord:
            flag = "true"
            score = 1
            print("Positive Word: "+findWord)
            break
        else:
            flag = "false"
    if flag == "false":
        for i in range(0, len(listOfNegativeWord)):
            if listOfNegativeWord[i] == findWord:
                flag = "true"
                score = -1
                print("Negative Word: "+ findWord)
                break
            else:
                flag = "false"

    return score

