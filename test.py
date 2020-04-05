import functionPython
import posTagger
from bnltk.stemmer import BanglaStemmer
from bnltk.tokenize import Tokenizers
t = Tokenizers()

dataParameter = "data/positive-data/positive-word.txt"
listOfPositiveWord = functionPython.LoadData(dataParameter)

#print(listOfSentence)

for i in range(0, len(listOfPositiveWord)):
    count = 0
    for j in range(0, len(listOfPositiveWord)):
        if listOfPositiveWord[i] == listOfPositiveWord[j]: #and count <= 1:
            count += 1
    if count > 1:
        print(listOfPositiveWord[i] + " vlue  " + str(count))




"""

from bnltk.stemmer import BanglaStemmer
from bnltk.tokenize import Tokenizers
t = Tokenizers()
#print(t.bn_word_tokenizer(' আমার সোনার বাংলা। , আমি তোমাকে ভালোবাসি ।'))
extract = t.bn_word_tokenizer('আবরার হত্যায় নির্ভুল অভিযোগ পত্র দেওয়ার চেস্টা করেছি')
print(extract)
test = 'চট্টগ্রাম'
if test == extract[1]:
    print("yes match")
else:
    print("no match")

bn_stemmer = BanglaStemmer()

for i in range(len(extract)):
    #print(extract[i])
    print(bn_stemmer.stem(extract[i]))

print(bn_stemmer.stem(extract[1]))

from bnltk.pos_tagger import PosTagger

p_tagger = PosTagger()
p_tagger.loader()
#sentences = 'দুশ্চিন্তার কোন কারণই নাই'
sentences = 'করিম হত্যায় নির্ভুল অভিযোগ পত্র দেওয়ার চেস্টা করেছি'

postText = p_tagger.tagger(sentences)
print(postText)
sentences = 'রাজু চট্টগ্রাম বাংলাদেশী সুশীল খুব অবশ্যই তুমি আমি আপনি এবং ও কিন্তু অথচ বরং তবে তখন লিখেছিল এসেছিল পড়তে ঘুমায়'
postText = p_tagger.tagger(sentences)
print(postText)

"""