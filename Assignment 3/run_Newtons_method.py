
# coding: utf-8

# # run_Newtons_method

# In[1]:

import numpy as np


# ## (b) VectorNewtonsMethod

# In[24]:

def VectorNewtonsMethod(fcn, Jacobian, x_orig, xtol):
    for i in range (0,21):
        x_change = np.linalg.solve(Jacobian(x_orig), -1*fcn(x_orig))
        if x_change > xtol:
            x_orig+=x_change
        else:
            break
    if i>20 or i==20:
        print "FAILED"
        
    return x_orig

# ## (c) Solve the given system of equations
# ### First, create the needed functions.

# In[16]:
#print e
# The function to find the roots of
def my_f(x):
    x1 =np.array([])
    x1.append( x[0]**2 + x[1]**2 -x[2]-1)
    x1.append( x[0]+ x[1]*x[2])
    x1.append(e**x[0]-1.0/2.0)
    return x1

# The function's Jacobian
def my_Jacobian(x):
    x1 =np.append([[2*x[0],2*x[1],-1],axis=0)
    x1 =np.append([1,x[2],x[1]],0)
    x1 =np.append([e**x[0],0,0],0)
    return x1
#my_Jacobian([1,2,3])

# ### Then call your VectorNewtonsMethod function
# (using a couple different initial guesses)
xtol = 10**-7
x_orig =np.array( [0,1,0])
VectorNewtonsMethod(my_f, my_Jacobian, x_orig, xtol )
# In[ ]:



