import numpy as np

# ## (b) VectorNewtonsMethod
def VectorNewtonsMethod(fcn, Jacobian, x_orig, xtol):
    for i in range (0,21):
        x_change = np.linalg.solve(Jacobian(x_orig), fcn(x_orig))
        if x_change.all() > xtol:
            x_orig+=x_change
        else:
            print("i ",i)
            break
    if i>20 or i==20:
        return "FAILED"
     
    return x_orig

# ## (c) Solve the given system of equations
# The function to find the roots of
def my_f(x):
    x1 =[]
    x1.append( x[0]**2 + x[1]**2 -x[2]-1)
    x1.append( x[0]+ x[1]*x[2])
    x1.append(e**x[0]-1.0/2.0)
    x1 = np.array(x1)*-1
    return x1
#print my_f([-0.69314718,321,234])
# The function's Jacobian
def my_Jacobian(x):
    x1=[]
    x1.append([2*x[0],2*x[1],-1])
    x1.append([1,x[2],x[1]])
    x1.append([e**x[0],0,0])
    return x1

xtol = 0.0000001
x_orig = [0.0,1.0,0.0]
print VectorNewtonsMethod(my_f, my_Jacobian, x_orig, xtol )
x_orig = [0.4,0.0,0.9]
print VectorNewtonsMethod(my_f, my_Jacobian, x_orig, xtol )





