'''
Created on May 21, 2016

@author: Edward
'''

import numpy as np, time, math

# Lecture 2
A = np.array([10.0,7.9,23.3])
print '\nA = \n',  A 

B = np.array([[1,2,3],[4,5,6],[7,8,9]])
print '\nB = \n',  B

C = np.array([ [1,2,3], \
               [4,5,6], \
               [7,8,9]])
print '\nC = \n',  C 

D = np.zeros((2,2,2))
print '\nD = \n',  D 

E = np.empty((3,2,2))
print '\nE = \n',  E 

F = np.ones((2,2,2,2))
print '\nF = \n',  F 

# Lecture 3
G = np.random.rand(2,2)
print '\nG = \n',  G 

H = np.random.rand(1,2)
print '\nH = \n',  H 

I = G - H 
print '\nI = \n', I 

J = G - H 
print '\nJ = \n', J 

K = np.ones((100,1))*2
print '\nK = \n', K[:3]

L = np.power(K, 2)
print '\nL = \n', L[:3]   

M = np.log(L)
print '\nM = \n', M[:3]

N = np.sin(M)
print '\nN = \n', N[:3]

# Lecture 4
O = np.random.rand(2,2)
print '\nO = \n',  O 

P = O.ravel()
print '\nP = \n',  P 
  
Q = np.reshape(P,(2,2))
print '\nQ = \n',  Q 

R = np.flipud(Q)
print '\nR = \n',  R 

S = np.fliplr(Q)
print '\nS = \n',  S

T = Q.T
print '\nT = \n',  T

U1 = np.random.rand(2,2)
U2 = np.random.rand(1,2)
U3 = np.random.rand(1,2)
print '\nU1 = \n',  U1
print '\nU2 = \n',  U2
print '\nU3 = \n',  U3
UC = np.concatenate((U1,U2,U3), axis=0)
print '\nUC = \n',  UC

V1 = np.random.rand(2,2)
V2 = np.random.rand(2,1)
V3 = np.random.rand(2,1)
print '\nV1 = \n',  V1
print '\nV2 = \n',  V2
print '\nV3 = \n',  V3
VC = np.concatenate((V1,V2,V3), axis=1)
print '\nVC = \n',  VC
 
# Lecture 5
W = np.random.rand(1000000,1)
X = np.random.rand(1000000,1)
start = time.time()
Y = np.tan(X/W)
elapsed = time.time() - start
print '\nelapsed with numpy = \n',  elapsed

start = time.time()
Y=[]
for w, x in zip(W,X):
    y = math.tan(x/w)
    Y.append(y)
elapsed = time.time() - start
print '\nelapsed with math = \n',  elapsed

# Lecture 6
A = np.random.rand(4,2)
A[1,0] = np.NaN
print '\nA = \n',  A
print '\nmean = \n',  np.mean(A,axis=0)
print '\nnanmean = \n',  np.nanmean(A,axis=0)

