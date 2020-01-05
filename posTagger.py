"""
it takes a word then gives which parts of speech it is as a tuple as 
(word,nameOfpos)
"""

from xml.dom import minidom

wordTuple = ()
nouns=[]
prons=[]
verbs=[]
adj=[]
adv=[]
conj=[]
def gettinNouns():
    xmldoc = minidom.parse('data/github/Noun.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nouns.append(s.childNodes[0].nodeValue)
def gettinProns():
    xmldoc = minidom.parse('data/github/Pronoun.xml')
    itemlist = xmldoc.getElementsByTagName('pron')
    for s in itemlist:
        prons.append(s.childNodes[0].nodeValue)
def gettinVerbs():
    xmldoc = minidom.parse('data/github/Verb.xml')
    itemlist = xmldoc.getElementsByTagName('verb')
    for s in itemlist:
        nouns.append(s.childNodes[0].nodeValue)
def gettinPosLen2():
    xmldoc = minidom.parse('data/github/L1_2.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen3():
    xmldoc = minidom.parse('data/github/L3.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen4():
    xmldoc = minidom.parse('data/github/L4.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen5():
    xmldoc = minidom.parse('data/github/L5.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen6():
    xmldoc = minidom.parse('data/github/L6.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen7():
    xmldoc = minidom.parse('data/github/L7.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen8():
    xmldoc = minidom.parse('data/github/L8.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen9():
    xmldoc = minidom.parse('data/github/L9.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen10():
    xmldoc = minidom.parse('data/github/L10.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen11():
    xmldoc = minidom.parse('data/github/L11.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen12():
    xmldoc = minidom.parse('data/github/L12.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen13():
    xmldoc = minidom.parse('data/github/L13.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen14():
    xmldoc = minidom.parse('data/github/L14.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen15():
    xmldoc = minidom.parse('data/github/L15.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen16():
    xmldoc = minidom.parse('data/github/L16.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen17():
    xmldoc = minidom.parse('data/github/L17.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen18():
    xmldoc = minidom.parse('data/github/L18.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen19():
    xmldoc = minidom.parse('data/github/L19.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen20():
    xmldoc = minidom.parse('data/github/L20.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
gettinNouns()
gettinPosLen2()
gettinPosLen3()
gettinPosLen4()
gettinPosLen5()
gettinPosLen6()
gettinPosLen7()
gettinPosLen8()
gettinPosLen9()
gettinPosLen10()
gettinPosLen11()
gettinPosLen12()
gettinPosLen13()
gettinPosLen14()
gettinPosLen15()
gettinPosLen16()
gettinPosLen17()
gettinPosLen18()
gettinPosLen19()
gettinPosLen20()
gettinProns()
gettinVerbs()


class pos:
    def posTagging(wordlist):
        global prons, adj, adv, conj, verbs, wordTuple
        PosWordList = []
        #print(prons)
        for i in range(0, len(wordlist)):
            if wordlist[i] in prons:
                wordTuple = (wordlist[i], "pron")
            elif wordlist[i] in adj:
                wordTuple = (wordlist[i], "adj")
            elif wordlist[i] in adv:
                wordTuple = (wordlist[i], "adv")
            elif wordlist[i] in conj:
                wordTuple = (wordlist[i], "conj")
            elif wordlist[i] in verbs:
                wordTuple = (wordlist[i], "verb")
            else:
                wordTuple = (wordlist[i], "N/A")
            PosWordList.append(wordTuple)

        return PosWordList


#a = pos()
#wordlist = ["এবং", "ও", "কিন্তু", "আর"]
#wordTuple = ()
#print(a.posTagging(wordlist))
