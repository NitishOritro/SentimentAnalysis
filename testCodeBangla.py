import re

test = "!"
string = "বাংলাদেশ!"

wordsDict = re.split(r'\s', string)

if test in string:
    print("yes match")
else:
    print("no match")


for i in range(len(wordsDict)):
    #print(extract[i])
    if test == wordsDict[i]:
        print("yes match")
    else:
        print("no match")

res = None
for i in range(0, len(string)):
    if string[i] == test:
        res = i + 1
        break

if res == None:
    print("No such charater available in string")
else:
    print("Character {} is present at {}".format(test, str(res)))