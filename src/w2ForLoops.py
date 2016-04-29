'''
Created on Apr 28, 2016

@author: Edward
'''
# For loop 1
myList = [1,2,3,4,5,6]

for val in myList:
    print val
    
    

# For loop 2
tempList = range(5)
print tempList
for val in range(5):
    print val
    

# For loop 3
startVal = 5
for _ in range(10):
    startVal = startVal**2/10.0
    print startVal