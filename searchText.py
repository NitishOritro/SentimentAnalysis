"""
Search a word in a file
"""

import functionPython

dataParameter = "data/Lexicon Dictionary Data/Resturant/correctPositive.txt"
listOfPositiveWord = functionPython.LoadData(dataParameter)
dataParameter = "data/Lexicon Dictionary Data/Resturant/correctNegative.txt"
listOfNegativeWord = functionPython.LoadData(dataParameter)

listOfTotalWord = listOfPositiveWord + listOfNegativeWord

#find a word
find = "অংশগুলির"
print("Positive found case match")
for i in range(0, len(listOfPositiveWord)):
    for j in range(0, len(listOfNegativeWord)):
        if listOfPositiveWord[i] == listOfNegativeWord[j]:
            print(listOfPositiveWord[i])
            break

print("Negative found case match")
for i in range(0, len(listOfNegativeWord)):
    for j in range(0, len(listOfPositiveWord)):
        if listOfNegativeWord[i] == listOfPositiveWord[j]:
            print(listOfNegativeWord[i])
            break

"""

#with open('data/positive-data/positive-word.txt', encoding="utf8") as myfile:
with open('data/Word-Dictionary/edit/BengaliWordList_40.txt', encoding="utf8") as myfile:
  data = myfile.read()
myfile.close()
#print(data)

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

print(listOfWord)


check dt redundncy in two text 
"""

