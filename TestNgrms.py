import functionPython

import functionPython
from collections import Counter
import xlrd
import posTagger
"""Load Dataset """

dataParameter = "data/Lexicon Dictionary Data/Restaurant/correctNegative.txt"
listOfPositiveWord = functionPython.LoadData(dataParameter)
dataParameter = "data/Lexicon Dictionary Data/Restaurant/correctPositive.txt"
listOfNegativeWord = functionPython.LoadData(dataParameter)

listOfStopWord = functionPython.LoadData("data/stop-word/stopWordModel.txt")

listOfTotalWord = listOfPositiveWord + listOfNegativeWord

from bnltk.tokenize import Tokenizers
t = Tokenizers()
from bnltk.stemmer import BanglaStemmer
from bnltk.tokenize import Tokenizers
t = Tokenizers()
fullStop = "।"

#Load Main Data

loc = ("data/main-data/Restaurant_Test.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)


def checkStopWordGram(extractToken):
    newExtractToken = []
    for wordExtract in extractToken:
        checkWord = functionPython.findWordFromList(listOfStopWord, wordExtract)
        if checkWord == "False":
            newExtractToken.append(wordExtract)

    return newExtractToken


def removeStopWord(Sentence):
    #print(Sentence)
    sentence = ""
    extractToken = checkStopWordGram(t.bn_word_tokenizer(Sentence))
    for wi in range(len(extractToken)):
        sentence = sentence+" "+extractToken[wi]
    return sentence


sentence = ""
listOfSentence = []
listOfTotalSentence = []

for i in range(1,4):
    data = sheet.cell_value(i, 1)
    for j in range(0, len(data)):
        lenData = len(data)
        if j == len(data)-1:
            lenData = len(data)
            sentence = sentence + data[j]
            listOfSentence.append(removeStopWord(sentence))
            sentence = ""
            break
        else:
            sentence = sentence + data[j]
    #print(listOfSentence)

    listOfTotalSentence.append(listOfSentence)
    listOfSentence = []


print(listOfTotalSentence)

"""
extractToken = t.bn_word_tokenizer(text)
print(extractToken)
gram = ""

extractToken = checkStopWordGram(t.bn_word_tokenizer(text))
print(extractToken)

for i in range(len(extractToken)):
    gram = gram+" "+extractToken[i]
    #print(gram)
    #ngrams[gram].append(words[i+n])

print(gram)

"""