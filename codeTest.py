"""
print("Hello World")

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
    print("")

numbers=[5,2,5,2,2,2]
"""


from bnltk.stemmer import BanglaStemmer
from bnltk.tokenize import Tokenizers
t = Tokenizers()
#print(t.bn_word_tokenizer(' আমার সোনার বাংলা। , আমি তোমাকে ভালোবাসি ।'))
extract = t.bn_word_tokenizer("আবরার হত্যায় নির্ভুল অভিযোগ পত্র দেওয়ার চেস্টা করেছি! ")
print(extract)

"""
test = 'চট্টগ্রাম'
if test == extract[1]:
    print("yes match")
else:
    print("no match")

"""
test = "!"
if test == "বাংলাদেশ !":
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
#sentences = 'আবরার হত্যায় নির্ভুল অভিযোগ পত্র দেওয়ার চেস্টা করেছি'
#sentences = "চাইতে হতে চেয়ে হইতে অপেক্ষা থেকে সবচাইতে সবথেকে সর্বাপেক্ষা সর্বাধিক অনেক অধিক অল্প বেশী অল্প কম অধিকতর গুরুতম গুরুতর দীর্ঘতম দীর্ঘতর"

sentences = " না নেই নই নাই নয়"

postText = p_tagger.tagger(sentences)
print(postText)


"""



from bnltk.stemmer import BanglaStemmer
bn_stemmer = BanglaStemmer()

print(bn_stemmer.stem('করেছ'))
print(bn_stemmer.stem('করলে'))
print(bn_stemmer.stem('করলো'))
print(bn_stemmer.stem('করেছে'))
print(bn_stemmer.stem('কর'))
print(bn_stemmer.stem('করতে'))
print(bn_stemmer.stem('করছিল'))
print(bn_stemmer.stem('করছিলে'))
print(bn_stemmer.stem('করছিলো'))
print(bn_stemmer.stem('করছিলে'))
print(bn_stemmer.stem('করতেছিলো'))
print(bn_stemmer.stem('করতেছিল'))
print(bn_stemmer.stem('করছিলে'))
print(bn_stemmer.stem('করতেছিলেন'))
print(bn_stemmer.stem('করছিলেন'))
print(bn_stemmer.stem('করবো'))
print(bn_stemmer.stem('করবেন'))
print(bn_stemmer.stem('করবি'))
print(bn_stemmer.stem('করবে'))


"""

"""



from bnltk.pos_tagger import PosTagger

p_tagger = PosTagger()
p_tagger.loader()
#sentences = 'দুশ্চিন্তার কোন কারণই নাই'
sentences = 'রাজু চট্টগ্রাম বাংলাদেশী সুশীল খুব অবশ্যই তুমি আমি আপনি এবং ও কিন্তু অথচ বরং তবে তখন লিখেছিল এসেছিল পড়তে ঘুমায়'
print(p_tagger.tagger(sentences))

"""


