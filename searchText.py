"""
Search a word in a file
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

#find a word
find = "অনাস্থা"
for i in range(0, len(listOfWord)):
    if listOfWord[i] == find:
        print("found case match")
        break
    else:
        print("not found")
