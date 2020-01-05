from bnltk.pos_tagger import PosTagger

p_tagger = PosTagger()
p_tagger.loader()



with open('data/Pronoun.txt', encoding="utf8") as myfile:
  data = myfile.read()
myfile.close()
print(data)


postText = p_tagger.tagger(data)
#print(postText)

for i in range(0, len(postText)):
    print(postText[i])

