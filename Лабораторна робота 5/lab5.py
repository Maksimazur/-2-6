import numpy as np
from scipy import optimize
from scipy.misc import derivative
import math
x0 = 0.4
y0 = 1
delta = 0.1
def f1(y):
    return math.sin(y + 0.5) - 1
def f2 (x):
    return math.cos(x - 2) * (-1)
def iter (x,y,e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print ('Simple iteration:')
    print ('x=', xn, '\ny=',yn,'\nThe amount of iteration = ',n)
iter(x0,y0,0.0001)
def f3(x):
    return 3*x[0] - math.cos(x[1]) - 0.9, math.sin(x[0] - 0.6) - x[1] -1.6
s = optimize.root(f3, [0.,0.], method = 'hybr')
print ('Chek',s.x)
print ('Chek',s.x)