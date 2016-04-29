'''
Created on Apr 28, 2016

@author: Edward Tadros
'''
import re

# Function 1 
def stringEvenOrOdd(inputString):
    string_len = len(inputString)
    if string_len % 2 == 0:
        evenOrOdd = 'even'
    else:
        evenOrOdd = 'odd'
    return evenOrOdd


# Function 2
def lowerList(inputList):    
    lowerList = [ s.lower() for s in inputList ]
    return lowerList




# Function 3
def wordCount(inputString):
    wCount = {}
    listString = inputString.split()
    for word in listString:
        if word in wCount:
            wCount[word] += 1
        else:
            wCount[word] = 1
    return wCount



# Function 4
def tupleCounts2Percents(inputList):
    # get total by using a list comprehension
    sumList = float(sum([ n[1] for n in inputList]))
    outputList = []
    for inputListTuple in inputList:
        outputList.append((inputListTuple[0],inputListTuple[1]/sumList))
    return outputList


# Function 5
def tupleTagCounts(inputList):
    outputList = []
    words = re.findall(r'\w+',str(inputList))
    inputDict = wordCount(' '.join(words))
    for w,c in inputDict.items():
        if c > 1:
            outputList.append((w,c))
    return outputList


# Function 6
def list2Unique(inputList):
    outputList = []
    for elem in inputList:
        if elem in outputList:
            continue
        else:
            outputList.append(elem)
    return outputList



# Function 7
def cumulativeSum(inputList):
    outputSum = sum(inputList)
    return outputSum



# Function 8
def returnWordsBetween(firstWord,secondWord,inputString):
    match = re.search(r'' + firstWord + ' (.*) ' + secondWord, inputString)
    list_words = match.group(1).split()
    return list_words
