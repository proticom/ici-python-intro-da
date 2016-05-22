'''
Created on May 14, 2016

@author: Edward
'''
#import Tadros_Edward_week4 as w4
import tadros_edward_week5np as w5
import numpy as np


#print w4.makeMap()

'''
    #latitudes = [41.8781, 40.7128, 34.0522]
    #longitudes = [-87.6298, 74.0059, 118.2437]
    
    latitudes = [41.50, 40.47, 34.30]
    longitudes = [87.37, 73.58, 118.15]
    
    latitudes = [41.50, 40.47, 34.30]
    longitudes = [-87.37, -73.58, -118.15]
    labels = ['Chicago', 'New York', 'Los Angeles']
'''
'''
A = np.array([[0.31903967,  0.49385635], 
              [0.13983727, -0.40484725]])
A[1,0] = np.NaN

A = np.array([[ 0.24439266,  0.10458247], \
               [    np.nan,   0.93138295], \
               [ 0.77060256,  0.64490737], \
               [ 0.24326940,  0.68065127]])
print '1', type(A)
print '2', A
print w5.normalizeArray(A)
'''

A = np.array([[ 0.24439266,  0.10458247], \
              [    np.nan,   0.93138295], \
              [ 0.77060256,  0.64490737], \
              [ 0.24326940,  0.68065127]])
print '\nArray\n---------------------------\n', A
print '\n#1\n---------------------------\n', w5.findSDArray(A)
print '\n#2\n---------------------------\n', w5.normalizeArray(A)
print '\n#3\n--------------------------\n', w5.negativesToZero(A)
