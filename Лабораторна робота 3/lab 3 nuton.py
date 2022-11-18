import numpy as np
import math
from scipy.misc import derivative
def f(x):
    return 3*pow(x,4) + 10*pow(x,3) + pow(x,2) - 5*x - 3
a = -3
b = 4

eps = 0.001

def nuton(a,b,eps):
    df2 = derivative(f, b, n = 2)
    if (f(b)*df2>0):
        xi = b
    else:
        xi = a
    df = derivative(f,xi, n= 1)
    xi_1 = xi - f(xi)/df
    while (abs(xi_1 - xi)>eps):
        xi = xi_1
        xi_1 = xi - f(xi)/df
    return print ('x =', xi_1)
nuton (a,b,eps)