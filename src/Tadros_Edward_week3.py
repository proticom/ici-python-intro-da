'''
Created on May 7, 2016

@author: Edward
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def loadAndPrepData(filepath):
    pd.set_option("display.width", 200)
    dataFrameRaw = pd.read_csv(filepath,header=0,sep='\t')
    dataFrame = dataFrameRaw[:638]
    return dataFrame

def onlyOneState(filepath, state):
    dataFrameRaw = loadAndPrepData(filepath)
    dataFrame = dataFrameRaw.loc[dataFrameRaw.State==state]
    return dataFrame

def sumStateCount(filepath, state):
    dataFrame = onlyOneState(filepath, state)
    return dataFrame['Count'].sum()

def listOfStates(filepath):
    dataFrameRaw = loadAndPrepData(filepath)
    return dataFrameRaw['State'].unique()
    
def cancerSums(filepath):
    dictCancerSums = {}
    allStates = listOfStates(filepath)
    for aState in allStates:
        dictCancerSums[aState]=sumStateCount(filepath, aState)
    return dictCancerSums

def stateCountAsList(filepath, state):
    yearList = range(1999,2012)
    countsList=[]
    dfStateSubset = onlyOneState(filepath, state)
    df = dfStateSubset.convert_objects(convert_numeric=True)
    #countList = df['Count'].tolist()
    for year in yearList:
        if year not in df['Year'].tolist():
            countsList.append(np.nan)
        else:
            countsList.append(float(df['Count'][df.Year==year]))
    return countsList
      
def getStateCountsDF(filepath):
    #create a list of lists of counts for each state
    listOfListCounts = []
    allStates = listOfStates(filepath)
    for aState in allStates:
        listOfListCounts.append(stateCountAsList(filepath, aState))
    
    # create a DataFrame from the list of list counts
    dataFrame = pd.DataFrame(listOfListCounts,index=allStates)
    return dataFrame
        
def plotCounts(filepath):
    dataFrame = getStateCountsDF(filepath)
    dfT = dataFrame.transpose()
    dfT.plot(legend=False)
    plt.show()

   
#df ='United+States+Cancer+Statistics%2C+1999-2011+Incidence.txt'
#st = 'Alabama'

#result = plotCounts(df)
#print result


