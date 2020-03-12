# Program to extract a particular row value
import functionPython
import xlrd
import posTagger

import xlwt
from xlwt import Workbook
import openpyxl

from bnltk.stemmer import BanglaStemmer
from bnltk.tokenize import Tokenizers
t = Tokenizers()
fullStop = "।"
questionMarkBN = "?"
questionMarkEN = "?"

""""""




"""Load Dataset """

dataParameter = "data/positive-data/positive-word.txt"
listOfPositiveWord = functionPython.LoadData(dataParameter)
dataParameter = "data/negative-word/negative-word.txt"
listOfNegativeWord = functionPython.LoadData(dataParameter)
dataParameter = "data/negative-word/neg.txt"
listOfNegWord = functionPython.LoadData(dataParameter)
dataParameter = "data/CCD-CCS/CCID.xlsx"
listOfcCDcCSWord = functionPython.LoadExcle(dataParameter)
dataParameter = "data/Adjective-Adverb/exel/jj-jq.xlsx"
listOfJJJQCSWord = functionPython.LoadExcle(dataParameter)
#print(listOfNegWord)

#Load Main Data

loc = ("data/main-data/Cricket.xlsx")

"""Load Dataset """

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

sentence = ""
listOfSentence = []
listOfSentenceQM = []
listOfSentenceScore = []
value=""

score = 1
scoreWord = 1
scoreWordQM = 1
scoreNegaWordCount = 0
scoreNegCount = "N/F"

cordinatingConjuction = 0
lengthOfExtract = 0
totalScoreOfSentence = 0
totalScoreOfSentenceQM = 0

finalScoreofSentence = 0

for i in range(1,30):
    data = sheet.cell_value(i, 2)
    for j in range(0, len(data)):
        lenData = len(data)
        if data[j] == fullStop:
            listOfSentence.append(sentence)
            sentence = ""
        elif data[j] == questionMarkBN:
            listOfSentenceQM.append(sentence)
            sentence = ""
        elif j == len(data)-1:
            lenData = len(data)
            sentence = sentence + data[j]
            listOfSentence.append(sentence)
            sentence = ""
            break
        else:
            sentence = sentence + data[j]
    print("jth value "+str(j)+" length of data "+str(lenData))
    print(listOfSentence)
    listOfSentence = []
"""

    for QM in range(0, len(listOfSentenceQM)):
        if listOfSentenceQM[QM] != "":
            #print(listOfSentenceQM[QM])
            extract = t.bn_word_tokenizer(listOfSentenceQM[QM])
            #print(extract)
            tokenizePostagger1 = posTagger.pos.posTagging(extract)
            if tokenizePostagger1[len(extract)-1][1] == 'verb':
                #print(tokenizePostagger1[len(extract)-1][0]+" found verb")
                scoreWordQM = -1
            else:
                scoreWordQM = 0
                listOfSentence.append(listOfSentenceQM[QM])
            #print("Result score: " + str(scoreWordQM))
            totalScoreOfSentenceQM = totalScoreOfSentenceQM + scoreWordQM

    #print("Total Score of a QM sentecne: " + str(totalScoreOfSentenceQM))

"""