from bnltk.tokenize import Tokenizers
t = Tokenizers()

from bnltk.tokenize import Tokenizers
t = Tokenizers()
fullStop = "।"



text = "আমি দুই সেকেন্ডের এলএ থেকে শহরে দুই বন্ধু সঙ্গে ছিল যখন আমি এই দ্বিতীয় তলায় ওয়াচ আপ উপর হোঁচট খেয়েছি, সুশীল লোকেদের গুরুতর হচ্ছে, আমরা অ্যাকশন কাছাকাছি হতে সুশি বার এ বসে ছিল।"


extractToken = t.bn_word_tokenizer(text)
print(extractToken)
gram = ""

print(extractToken[2])
for i in range(len(extractToken)):
    gram = gram+" "+extractToken[i]
    #print(gram)
    #ngrams[gram].append(words[i+n])

print(gram)