#! /usr/local/bin/python3.4

def loadFile():

    with open("signals.txt", "r") as signalFile:
        lines = signalFile.readlines()

    return lines


def getAverageBySignal(signalName):
    file = loadFile();

    collist = file[0].split()
    if not signalName in collist:
        return None

    colindex = collist.index(signalName) + 1

    sum = 0
    size = 0
    for line in file[2:]:
        collist = line.split()
        sum = sum + float(collist[colindex])
        size = size + 1

    return round(sum/size, 2)


def getAverageByDay(day):
    file = loadFile();
    sum = 0
    size = 0

    for line in file[2:]:
        list = line.split()
        if list[0] == day:
            for val in list[1:]:
                sum += float(val)
                size += 1
    #if date doesnt exist
    if size < 1:
        return None

    return round(sum/size, 2)

def split(l, n):

    splist = []
    sublist = []

    for val in l:



        if len(sublist) >= n:
            #splist.append(sublist.copy())
            splist.append(sublist)
            #splist += sublist
            #print(splist)
            print("sublist " + str(sublist))
            print("splist" + str(splist))
            sublist = []
        #print(sublist)
        sublist.append(val)
        #print(len(sublist))

    splist.append(sublist)
    return splist


def getPalindromes():
    palSet = set()
    for x in range(100,1000):
        for y in range(100,1000):
            prod = str(x * y)
            if isPalindrome(prod):
                palSet.add(int(prod))
    palList = list(palSet)
    palList.sort()
    #print(palList)

    #print(palList)

    return palList

def isPalindrome(s):
    end = len(s) - 1
    start = 0
    if len(s) != 6:
        return False

    while start <= end:
        if s[start] != s[end]:
            return False
    start = start
    print(palList)

    return palList

def isPalindrome(s):
    end = len(s) - 1
    start = 0
    if (len(s)!= 6):
        return False

    while start <= end:
        if s[start] != s[end]:
            return False
        start = start + 1
        end = end - 1
    return True

def getWords(sentence, c):

    wordlist = []
    slist = sentence.split()
    for word in slist:
        if c == word[0] or c == word[-1]:
             if not word in wordlist:
                 wordlist.append(word)

    return wordlist



def getCumulativeSum():

    list = []
    sumlist = []
    for i in range(1,101):
        list.append(i)
        sumlist.append(sum(list))

    return sumlist


def transpose(mat):
    tmat = list(zip(*mat))
    return tmat



def partition(stream):
    prev = stream[0]
    list = []
    slist = []
    list.append(prev)
    for val in stream[1:]:
        if val == "0" and prev == val:
            list.append(val)
        elif val == "1" and prev == val:
            list.append(val)
        else:
            slist.append("".join(list))
            list = []
            prev = val
            list.append(prev)
    slist.append("".join(list))
    return slist

def getTheSolution():
    pass

if __name__ == "__main__":

    print(getAverageBySignal("T1"))
    print(getAverageByDay("03/12"))

    l = [11,18,15,21,19,13,14,17]
    print(split(l, 3))

    sentence = "the power of this engine matches that of the one we had last year"
    print(getWords(sentence, "e"))

    print(getCumulativeSum())

    mat = [[9,1],[1,3],[3,1]]
    print(transpose(mat))

    stream = "0001111110111100000100"
    print(partition(stream))

    print("New Function")
    # figure out how to check
    l = getPalindromes()
    print(len(l))