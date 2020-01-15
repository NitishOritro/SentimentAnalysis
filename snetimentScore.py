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

""""""




"""Load Positive Dataset """

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

loc = ("data/main-data/Restaurant.xlsx")

"""Load Dataset """

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

sentence = ""
listOfSentence = []
listOfSentenceScore = []
value=""

score = 1
scoreWord = 1
scoreNegaWordCount = 0
scoreNegCount = "N/F"

cordinatingConjuction = 0
lengthOfExtract = 0
totalScoreOfSentence = 0

for i in range(1,5):
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

        print("totral Length " + str(len(extract)))
        lengthOfExtract = len(extract) / 2
        for kk in range(0, len(extract)):
            if tokenizePostagger1[kk][1] == 'conj':
                print("conj " + str(kk))
                for ll in range(0, len(listOfcCDcCSWord)):
                    if ll != 0 and listOfcCDcCSWord[ll][0] == tokenizePostagger1[kk][0] and listOfcCDcCSWord[ll][1] == 1:
                        if kk >= lengthOfExtract:
                            cordinatingConjuction = kk
                            print("actual conj " + str(kk))
                            #print("conjunction word " + tokenizePostagger1[kk][0])
                            #if tokenizePostagger1[kk][0]
                            #print(listOfSentence[k])

        #print(tokenizePostagger1)

        for l in range(0, len(tokenizePostagger1)):
            value = tokenizePostagger1[l][0]
            if tokenizePostagger1[l][1] != 'pron':
                #check in positive negative dataset
                score = functionPython.LoadPositiveNegativeData(listOfPositiveWord, listOfNegativeWord, tokenizePostagger1[l][0])
                if score == -999:
                    score = 1
                    scoreNegCount = functionPython.CountNegativeData(listOfNegWord, tokenizePostagger1[l][0])
                    if scoreNegCount == "True":
                        scoreNegaWordCount = scoreNegaWordCount + 1
                    elif tokenizePostagger1[l][1] == 'conj':
                        value = tokenizePostagger1[l][0]
                        if l == cordinatingConjuction:
                            scoreWord = scoreWord * 2
                        else:
                            score = functionPython.cCDcCSData(listOfcCDcCSWord, tokenizePostagger1[l][0])
                        #scorecCDcCSWordScoreValue = functionPython.cCDcCSData(listOfcCDcCSWord, tokenizePostagger1[l][0])
                    elif tokenizePostagger1[l][1] == 'adj' or  tokenizePostagger1[l][1] == 'adv':
                        value = tokenizePostagger1[l][0]
                        score = functionPython.JJJQData(listOfJJJQCSWord, tokenizePostagger1[l][0])
                        #scorecCDcCSWordScoreValue = functionPython.JJJQData(listOfJJJQCSWord, tokenizePostagger1[l][0])

            scoreWord = scoreWord * score

        #print("Neg count: " + str(scoreNegaWordCount))
        print("total neg counted word "+ str(scoreNegaWordCount))
        if scoreNegaWordCount%2 != 0:
            scoreWord = scoreWord * (-1)

        print("Result score: "+str(scoreWord))
        totalScoreOfSentence = totalScoreOfSentence + scoreWord
        scoreWord = 1

    print("Total Score of a sentecne: " + str(totalScoreOfSentence))

    #ADD Result in Excle
    listOfSentenceScore.append(totalScoreOfSentence)


    totalScoreOfSentence = 0
    scoreNegaWordCount = 0
    listOfSentence = []
functionPython.SaveData(listOfSentenceScore)
print(listOfSentenceScore)


"""
for i in range(0, len(listOfSentence)):
    print(listOfSentence[i])
"""


