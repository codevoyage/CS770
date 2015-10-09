
# coding: utf-8

# # photo_time
# We also import "sun_angle", which contains the function "sun_azel", supplied by Prof. G. Ometry.

# In[ ]:

import numpy as np
import matplotlib.pylab as plt
plt.ion()
import sun_angle


# Here is how we run Prof. Ometry's function.

# In[ ]:

# type
#   ? sun_angle.sun_azel
# for the function's documentation
#get_ipython().magic(u'pinfo sun_angle.sun_azel')


# In[ ]:
'''
azel = sun_angle.sun_azel(18.)   # h=18 is 6:00pm
print 'Azimuth A =', azel[0], ', Elevation E =', azel[1]
'''

# ## Some root-finding methods
# Here is where you write a function that implements one of the root-finding methods.
# 
# Here are some example templates for root-finding methods.

# In[ ]:

# Fixed-Point Iteration
def FixedPointIteration(x0, phi):
    # Your code here
    return x0


# In[ ]:

# Secant Method
def SecantMethod(x0,x1,fcn):
    # Your code here
    tol = 0.001
    
    while(abs(fcn(x1))>tol):
        t = x1 
        x1 = x0 + fcn(x0)[1]*((fcn(x1)[1]-fcn(x0)[1])/(x1-x0))
        x0 = t
    return x1


# In[ ]:

# Bisection Method
def BisectionMethod(x0,x1,fcn,E):
    #stopping Criterion
    tol = 0.00001
    fx = lambda x: fcn(x)[1]
    while abs(x0-x1) > tol:   
        d = (x0+x1)/2.0,
     
        if fx(x0)*fx(x1) < 0:
            x1 = d
        else:
            x0 = d

            
    return d


# ## Data from the photo
# How long is the shadow, and what elevation angle does that give us?

# In[ ]:

E = 17.23528526
print 'Elevation angle is', E, 'degrees'


# ## Call the solver to find h
#h = SecantMethod(0,24,sun_angle.sun_azel)
h= BisectionMethod(-24,24,sun_angle.sun_azel, E)
print "Hours: ", h

'''
azel = sun_angle.sun_azel(h)   # h=18 is 6:00pm
print 'Azimuth A =', azel[0], ', Elevation E =', azel[1]
'''

# In[ ]:



