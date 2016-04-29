'''
Created on Apr 28, 2016

@author: Edward
'''
def stringEvenOrOdd(string):
    string_len = len(string)
    if string_len % 2 == 0:
        evenOrOdd = 'even'
    else:
        evenOrOdd =  'odd'
    return evenOrOdd, string_len