
"""
it takes a word then discard some character if needed and convert the word
into its source word.Eg: "মেঘের" stemm to "মেঘ"
"""
from xml.dom import minidom

nounLen2 = []
nounLen3 = []
nounLen4 = []
nounLen5 = []
nounLen6 = []
nounLen7 = []
nounLen8 = []
nounLen9 = []
nounLen10 = []
nounLen11 = []
nounLen12 = []
nounLen13 = []
nounLen14 = []
nounLen15 = []
nounLen16 = []
nounLen17 = []
nounLen18 = []
nounLen19 = []
nounLen20 = []
nouns = []


def gettinNouns():
    xmldoc = minidom.parse('data/github/Noun.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nouns.append(s.childNodes[0].nodeValue)


def gettinNounLen2():
    xmldoc = minidom.parse('data/github/L1_2.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen2.append(s.childNodes[0].nodeValue)


def gettinNounLen3():
    xmldoc = minidom.parse('data/github/L3.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen3.append(s.childNodes[0].nodeValue)


def gettinNounLen4():
    xmldoc = minidom.parse('data/github/L4.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen4.append(s.childNodes[0].nodeValue)


def gettinNounLen5():
    xmldoc = minidom.parse('data/github/L5.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen5.append(s.childNodes[0].nodeValue)


def gettinNounLen6():
    xmldoc = minidom.parse('data/github/L6.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen6.append(s.childNodes[0].nodeValue)


def gettinNounLen7():
    xmldoc = minidom.parse('data/github/L7.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen7.append(s.childNodes[0].nodeValue)


def gettinNounLen8():
    xmldoc = minidom.parse('data/github/L8.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen8.append(s.childNodes[0].nodeValue)


def gettinNounLen9():
    xmldoc = minidom.parse('data/github/L9.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen9.append(s.childNodes[0].nodeValue)


def gettinNounLen10():
    xmldoc = minidom.parse('data/github/L10.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen10.append(s.childNodes[0].nodeValue)


def gettinNounLen11():
    xmldoc = minidom.parse('data/github/L11.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen11.append(s.childNodes[0].nodeValue)


def gettinNounLen12():
    xmldoc = minidom.parse('data/github/L12.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen12.append(s.childNodes[0].nodeValue)


def gettinNounLen13():
    xmldoc = minidom.parse('data/github/L13.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen13.append(s.childNodes[0].nodeValue)


def gettinNounLen14():
    xmldoc = minidom.parse('data/github/L14.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen14.append(s.childNodes[0].nodeValue)


def gettinNounLen15():
    xmldoc = minidom.parse('data/github/L15.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen15.append(s.childNodes[0].nodeValue)


def gettinNounLen16():
    xmldoc = minidom.parse('data/github/L16.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen16.append(s.childNodes[0].nodeValue)


def gettinNounLen17():
    xmldoc = minidom.parse('data/github/L17.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen17.append(s.childNodes[0].nodeValue)


def gettinNounLen18():
    xmldoc = minidom.parse('data/github/L18.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen18.append(s.childNodes[0].nodeValue)


def gettinNounLen19():
    xmldoc = minidom.parse('data/github/L19.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen19.append(s.childNodes[0].nodeValue)


def gettinNounLen20():
    xmldoc = minidom.parse('data/github/L20.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen20.append(s.childNodes[0].nodeValue)


gettinNouns()
gettinNounLen2()
gettinNounLen3()
gettinNounLen4()
gettinNounLen5()
gettinNounLen6()
gettinNounLen7()
gettinNounLen8()
gettinNounLen9()
gettinNounLen10()
gettinNounLen11()
gettinNounLen12()
gettinNounLen13()
gettinNounLen14()
gettinNounLen15()
gettinNounLen16()
gettinNounLen17()
gettinNounLen18()
gettinNounLen19()
gettinNounLen20()


class Stemmer:

    def wordStem(self, s):
        global nouns, nounLen2, nounLen3, nounLen4, nounLen5, nounLen6, nounLen7, nounLen8
        global nounLen10, nounLen11, nounLen12, nounLen13, nounLen14, nounLen15, nounLen16
        global nounLen9, nounLen17, nounLen18, nounLen19, nounLen20
        n1 = nouns + nounLen2 + nounLen3 + nounLen4 + nounLen5 + nounLen6 + nounLen7 + nounLen8
        n2 = nounLen10 + nounLen11 + nounLen12 + nounLen13 + nounLen14 + nounLen15 + nounLen16
        n3 = nounLen9 + nounLen17 + nounLen18 + nounLen19 + nounLen20
        allNouns = n1 + n2 + n3
        l = len(s)
        for i in range(l):
            stemmWord = s[:l - i]
            if stemmWord in allNouns:
                return stemmWord
        return s

print(Stemmer().wordStem("খেলোয়াড়দের"))