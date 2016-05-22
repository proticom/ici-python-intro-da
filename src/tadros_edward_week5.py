'''
Created on May 21, 2016

@author: Edward
'''
import numpy as np

def isNumpyArray(A):
    if type(A).__module__+'.'+type(A).__name__ == 'numpy.ndarray':
        res = True
    else:
        res = False
    return res
 
def makeNumpyArray(A): 
    if isNumpyArray(A)==False:
        A = np.array(A)
    return A 

def findSDArray(A):
    stdA = np.nanstd(A, axis=0)
    return stdA

def normalizeArray(A):
    A = makeNumpyArray(A)
    stdA = findSDArray(A)
    normA = A/stdA
    return normA

def negativesToZero(A):
    A = makeNumpyArray(A)
    A[np.nan_to_num(A)<0]=0
    return A
    
    