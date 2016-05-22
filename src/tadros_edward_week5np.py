'''
Created on May 21, 2016

@author: Edward
'''
import numpy as np

def findSDArray(A):
    stdA = np.nanstd(A, axis=0)
    return stdA

def normalizeArray(A):
    stdA = findSDArray(A)
    normA = A/stdA
    return normA

def negativesToZero(A):
    A[np.nan_to_num(A)<0]=0
    return A
    
    