# coding: utf-8

# # photo_time
# We also import "sun_angle", which contains the function "sun_azel", supplied by Prof. G. Ometry.

# In[ ]:

import numpy as np
import math
import matplotlib.pylab as plt
plt.ion()
import sun_angle


# Bisection Method
def BisectionMethod(x0,x1,fcn):
    #stopping Criterion
    tol = 0.0000000000001
    fx = lambda x: fcn(x)[1] - E 
    while abs(x0-x1)> tol:   
        d = (x0+x1)/2.0
        if (fx(x0)*fx(d)) < 0:
            x1 = d
        else:
            x0 = d 
    if sun_angle.sun_azel(d)[0]<200:
        return BisectionMethod(d+tol,24,fcn)    
    return x0


E = 17.23528526
print 'Elevation angle is', E, 'degrees'


h= BisectionMethod(0,24,sun_angle.sun_azel)
print "Hours: ", int(math.modf(h)[1]),', Minutes: ', int(round(math.modf(h)[0]*60))

azel = sun_angle.sun_azel(h)   # h=18 is 6:00pm
print 'Azimuth A =', azel[0], ', Elevation E =', azel[1]
