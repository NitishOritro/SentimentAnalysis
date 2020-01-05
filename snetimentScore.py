# Program to extract a particular row value
import functionPython
import xlrd
import posTagger
from bnltk.stemmer import BanglaStemmer
from bnltk.tokenize import Tokenizers
t = Tokenizers()
fullStop = "।"

""""""

scoreWord = 0


"""Load Positive Dataset """

dataParameter = "data/positive-data/positive-word.txt"
listOfPositiveWord = functionPython.LoadData(dataParameter)
dataParameter = "data/negative-word/negative-word.txt"
listOfNegativeWord = functionPython.LoadData(dataParameter)
dataParameter = "data/negative-word/neg.txt"
listOfNegWord = functionPython.LoadData(dataParameter)
print(listOfNegWord)
"""END """

"""Load Dataset """

loc = ("data/main-data/Restaurant.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

sentence = ""
listOfSentence = []



for i in range(1, 5):
    data = sheet.cell_value(i, 1)
    for j in range(0, len(data)):
        if data[j] == fullStop:
            listOfSentence.append(sentence)
            sentence = ""
            # break
        else:
            sentence = sentence + data[j]
    print(listOfSentence)

    for k in range(0, len(listOfSentence)):
        #print(listOfSentence[k])
        extract = t.bn_word_tokenizer(listOfSentence[k])
        #print(extract)
        tokenizePostagger1 = posTagger.pos.posTagging(extract)
        #print(tokenizePostagger1)

        for l in range(0, len(tokenizePostagger1)):
            if tokenizePostagger1[l][1] != 'pron':
                #check in positive dataset
                score = functionPython.LoadPositiveData(listOfPositiveWord, listOfNegativeWord, tokenizePostagger1[l][0])
                #print(tokenizePostagger1[l][0])
                scoreWord = scoreWord + score

        print(scoreWord)
        scoreWord = 0
    listOfSentence = []


"""
for i in range(0, len(listOfSentence)):
    print(listOfSentence[i])
"""


