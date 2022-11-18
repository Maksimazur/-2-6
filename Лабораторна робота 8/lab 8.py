import numpy as np
import matplotlib.pyplot as plt
from math import factorial

x=[3.50, 3.55, 3.60, 3.65, 3.70, 3.75, 3.80, 3.85, 3.90, 3.95, 4.00]
y=[33.1154, 34.8133, 36.5982, 38.4747, 40.4473, 42.5211, 44.7012, 46.9931, 49.4024, 51.9354, 54.5982]
h = x[1] -x[0]

x1=3.522
x2=3.905
x3=3.643
x4=4.005
x5=3.675
x6=3.852

q1 = (x1 - x[0])/h
q2 = (x2 - x[-1])/h
q3 = (x3 - x[0])/h
q4 = (x4 - x[-1])/h
q5 = (x5 - x[0])/h
q6 = (x6 - x[-1])/h

def n(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] -y[i-1])
    mas.pop(0) 
    if j == 1:
        return mas
    else:
        j-=1
        return n(mas, j)

#Перша інтерполяційна формула Ньютона
def Newton1(q):
    s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
    s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
    s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
    s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
    s_5 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*n(y,6)[0]/factorial(6)
    s_6 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*n(y,7)[0]/factorial(7)
    s_7 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*n(y,8)[0]/factorial(8)
    s_8 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*(q-8)*n(y,9)[0]/factorial(9)
    s_9 = q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*(q-8)*(q-9)*n(y,10)[0]/factorial(10)
    n_1 = s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7 + s_8 + s_9
    return n_1

#Друга інтерполяційна формула Ньютона
def Newton2(q1):
    s_1 = y[10]+q1*n(y,1)[9]+q1*(q1+1)*n(y,2)[8]/factorial(2)
    s_2 = q1*(q1+1)*(q1+2)*n(y,3)[7]/factorial(3)
    s_3 = q1*(q1+1)*(q1+2)*(q1+3)*n(y,4)[6]/factorial(4)
    s_4 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*n(y,5)[5]/factorial(5)
    s_5 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*n(y,6)[4]/factorial(6)
    s_6 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*n(y,7)[3]/factorial(7)
    s_7 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*(q1+7)*n(y,8)[2]/factorial(8)
    s_8 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*(q1+7)*(q1+8)*n(y,9)[1]/factorial(9)
    s_9 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*(q1+7)*(q1+8)*(q1+9)*n(y,10)[0]/factorial(10)
    n_2 = s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7 + s_8 + s_9
    return n_2

print ('The value of a function at a point x1=', x1, 'using Newton*s First Interpolation Formula', round(Newton1(q1),5))
print ('The value of a function at a point x2=', x2, 'using Newton*s Second Interpolation Formula', round(Newton2(q2),5))
print ('The value of a function at a point x3=', x3, 'using Newton*s First Interpolation Formula', round(Newton1(q3),5))
print ('The value of a function at a point x4=', x4, 'using Newton*s Second Interpolation Formula', round(Newton2(q4),5))
print ('The value of a function at a point x5=', x5, 'using Newton*s First Interpolation Formula', round(Newton1(q5),5))
print ('The value of a function at a point x6=', x6, 'using Newton*s Second Interpolation Formula', round(Newton2(q6),5))

#Графік
plt.plot(x, y, x1, Newton1(q1), 'ro', x2, Newton2(q2), 'ro', x3, Newton1(q3), 'ro', x4, Newton2(q4), 'ro', x5, Newton1(q5), 'ro', x6, Newton2(q6), 'ro')
plt.title('Interpolation')
plt.grid(True)
plt.show()