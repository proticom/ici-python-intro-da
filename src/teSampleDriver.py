'''
Created on Apr 28, 2016

@author: Edward
'''
import Tadros_Edward_week2

# Function 1
a = 'eencvd'
print Tadros_Edward_week2.stringEvenOrOdd(a)


# Function 2
l = ['Apple', 'BANANA', 'OraNge', 'pear']
print Tadros_Edward_week2.lowerList(l)

# Function 3
s = 'I like small dogs and big dogs'
print Tadros_Edward_week2.wordCount(s)

# Function 4
tl = [('CA', 1001), ('NY', 345), ('AZ', 123)]
print Tadros_Edward_week2.tupleCounts2Percents(tl)

# Function 5
tl2 = [('love', 'family'), ('dinner', 'family', 'nomnom'), ('wedding', 'romance', 'love')]
print Tadros_Edward_week2.tupleTagCounts(tl2)

# Function 6
l_six = [5,5,'apple','pizza','apple'] 
print Tadros_Edward_week2.list2Unique(l_six)

# Function 7
l_seven = [11,3,4.6]
print Tadros_Edward_week2.cumulativeSum(l_seven)

# Function 8
fW = '<data>'
sW = '</data>'
inStr = 'fooz bizz <data> 31.25 funnel </data> fuzz'
print Tadros_Edward_week2.returnWordsBetween(fW, sW, inStr)