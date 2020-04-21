import random
import nltk
from collections import Counter
from bnltk.tokenize import Tokenizers
t = Tokenizers()


import functionPython
from collections import Counter
import xlrd
import posTagger
import heapq
import xlwt
from xlwt import Workbook
import openpyxl
import numpy as np

from bnltk.stemmer import BanglaStemmer
from bnltk.tokenize import Tokenizers
t = Tokenizers()
fullStop = "।"

#Load Main Data

loc = ("data/main-data/Restaurant_Test.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)


"""Load Dataset """

dataParameter = "data/Lexicon Dictionary Data/Restaurant/correctNegative.txt"
listOfPositiveWord = functionPython.LoadData(dataParameter)
dataParameter = "data/Lexicon Dictionary Data/Restaurant/correctPositive.txt"
listOfNegativeWord = functionPython.LoadData(dataParameter)

listOfStopWord = functionPython.LoadData("data/stop-word/stopWordModel.txt")

listOfTotalWord = listOfPositiveWord + listOfNegativeWord


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
            listOfSentence.append(sentence)
            sentence = ""
            break
        else:
            sentence = sentence + data[j]
    #print(listOfSentence)
    listOfTotalSentence.append(listOfSentence)
    listOfSentence = []
#print(listOfTotalSentence)

# Building the model
# Order of the grams
n = 2
# Our N-Grams
ngrams = {}
###### Term Frequency(TF) calculation in wordToCount (No. of words in a doc) ######

def checkStopWordGram(extractToken):
    for wordExtract in extractToken:
        checkWord = functionPython.findWordFromList(listOfStopWord, wordExtract)
        if checkWord == "True":
            extractToken.remove(wordExtract)

    return extractToken

wordToCount = {}

checkWord = ""
for i in range(0, len(listOfTotalSentence)):
    extractToken = t.bn_word_tokenizer(listOfTotalSentence[i][0])
    extractToken = checkStopWordGram(extractToken)
    for i in range(len(extractToken)+1 - n):
        wordGram = ' '.join(extractToken[i:i + n])
        if wordGram not in wordToCount.keys():
            wordToCount[wordGram] = 1
        else:
            wordToCount[wordGram] += 1

#print(wordToCount)
sentence = ""
wordToCountInDOC = {}

for i in range(0, len(listOfTotalSentence)):
    doc = listOfTotalSentence[i][0]
    extractToken = t.bn_word_tokenizer(listOfTotalSentence[i][0])
    extractToken = checkStopWordGram(extractToken)
    sentence = ""
    for wi in range(len(extractToken)):
        sentence = sentence+" "+extractToken[wi]
    for word in wordToCount:
        if word in sentence:
            if word not in wordToCountInDOC.keys():
                wordToCountInDOC[word] = 1
            else:
                wordToCountInDOC[word] += 1


#print("wordToCountINDOC list ")
wordToCountINDOC = (sorted(wordToCountInDOC.items(), key=lambda x: x[1], reverse=True))
k = Counter(wordToCountINDOC)

wordToCountFreInDoc = k.most_common(20)
#print(wordToCountFreInDoc)

#print("wordToCountFre list ")
wordToCountFRE = (sorted(wordToCount.items(), key=lambda x: x[1], reverse=True))
k = Counter(wordToCountFRE)

wordToCountFre = k.most_common(20)
#print(wordToCountFre)


word_idfs1 = {}
word_idfs2 = {}
NoOfDocuments = len(listOfTotalSentence)


for word in wordToCountFreInDoc:
    doc_count = word[0][1]
    word_idfs2[word[0][0]] = np.log((NoOfDocuments / doc_count) + 1)

#print(word_idfs2)

for word in wordToCountFre:
    print(word[0][0])




###### Term Frequency(TF) Calculation ######

tf_matrix = {}
for word in wordToCountFre:
    doc_tf = []
    for i in range(0, len(listOfTotalSentence)):
        frequency = 0
        extractToken = t.bn_word_tokenizer(listOfTotalSentence[i][0])
        extractToken = checkStopWordGram(extractToken)
        for j in range(len(extractToken)+1 - n):
            wordGram = ' '.join(extractToken[j:j + n])
            if word[0][0] in wordGram:
                frequency += 1
        tf_word = frequency / (len(extractToken)-1)
        doc_tf.append(tf_word)
    tf_matrix[word[0][0]] = doc_tf


print("Term Frequency Matrix")
print(tf_matrix)


########### TF-IDF Calculation #############

tfIdf_matrix = []
for word in tf_matrix.keys():
    tfidf = []
    for tf in tf_matrix[word]:
        score = tf * word_idfs2[word]
        tfidf.append(score)
    tfIdf_matrix.append(tfidf)

for i in range(0, len(tfIdf_matrix)):
    print(tfIdf_matrix[i])


















"""

for word in wordToCountFre:
    doc_count = 0
    for data in listOfTotalSentence:
        extractToken = t.bn_word_tokenizer(data[0])  #extracttoken is a list
        #sentenceWordGram = wordGram(extractToken)
        for i in range(len(extractToken)+1 - n):
            wordGram = ' '.join(extractToken[i:i + n])
            if word[0][0] in wordGram:                                     #Word is tupple
                doc_count += 1
    word_idfs1[word[0][0]] = np.log((NoOfDocuments / doc_count) + 1)
    #print(str(doc_count)+" "+str(word[0]))
print(word_idfs1)




def wordGram(extractToken):

    for i in range(len(extractToken) - n):
        gram = ' '.join(extractToken[i:i + n])
        print(gram)
        if gram not in ngrams.keys():
            ngrams[gram] = 1
        else:
            ngrams[gram] += 1
        # ngrams[gram].append(words[i+n])
    wordToCount = (sorted(ngrams.items(), key=lambda x: x[1], reverse=True))
    print(wordToCount)



extractToken = t.bn_word_tokenizer(text)

for i in range(len(extractToken)-n):
    gram = ' '.join(extractToken[i:i+n])
    print(gram)
    if gram not in ngrams.keys():
        ngrams[gram] = 1
    else:
        ngrams[gram] += 1
    #ngrams[gram].append(words[i+n])

print(ngrams)
"""