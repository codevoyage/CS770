# -*- coding: utf-8 -*-

import numpy as np

a = np.array([30.,7.,-90.,45.,20.,-12.])
a = -1*a/a[0]
a = np.delete(a,0)

#print a

n = len(a)

#Generate Matrix to pass to the function
A = [[1 if i==j else 0 for i in range (0,n)] for j in range(0,n-1)]
A.insert(0,a)

#print A
#Compute Eigen V
v,w = np.linalg.eig(A)

print "The roots of the equation are: "+ str(v)