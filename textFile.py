
import posTagger
from bnltk.stemmer import BanglaStemmer
from bnltk.tokenize import Tokenizers
t = Tokenizers()

#from bnltk.pos_tagger import PosTagger
#p_tagger = PosTagger()
#p_tagger.loader()


punctuation = "!"
fullStop = "।"

with open('data/CCD-CCS/ptest.txt', encoding="utf8") as myfile:
  data = myfile.read()
myfile.close()
#print(data)

sentence = ""
listOfSentence = []

res = None
for i in range(0, len(data)):
    if data[i] == fullStop:
        res = i
        listOfSentence.append(sentence)
        sentence = ""
        #break
    else:
        sentence = sentence + data[i]

#print(listOfSentence)

for i in range(0, len(listOfSentence)):
    #print(listOfSentence[i])
    extract = t.bn_word_tokenizer(listOfSentence[i])
    #print(extract)
    tokenizePostagger1 = posTagger.pos.posTagging(extract)
    #print(tokenizePostagger1)


    for j in range(0, len(tokenizePostagger1)):
        if tokenizePostagger1[j][1] != 'conj':
            print(tokenizePostagger1[j][0] + " " + tokenizePostagger1[j][1])

    """
    #tokenizePostagger = p_tagger.tagger(listOfSentence[i])
    #print(tokenizePostagger)
    #for j in range(0, len(tokenizePostagger)):
        #if tokenizePostagger[j][1] != 'PPR' and tokenizePostagger[j][1] != 'PRP' and tokenizePostagger[j][1] != 'DAB' and tokenizePostagger[j][1] != 'PWH' and tokenizePostagger[j][1] != 'PRF':
        #if tokenizePostagger[j][1] != 'CCD' and tokenizePostagger[j][1] != 'CSB' and tokenizePostagger[j][1] != 'DRL':
        #print(tokenizePostagger[j][0]+" "+tokenizePostagger[j][1])

#print(tokenizePostagger1)



#print(extract)

#for i in range(0, len(listOfSentence)):
#    print(listOfSentence[i])

#print(sentence)
#print(listOfSentence)


if res == None:
    print("No such charater available in string")
else:
    print("Character {} is present at {}".format(fullStop, str(res)))
"""















