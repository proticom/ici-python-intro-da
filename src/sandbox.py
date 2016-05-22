'''
Created on May 22, 2016

@author: Edward
'''
import numpy as np

A = np.array([ [1,2], [4,np.nan] ])
B = np.array([ [1,1]])
C = np.concatenate([A,B],axis=0)



print np.mean(C)
print C
