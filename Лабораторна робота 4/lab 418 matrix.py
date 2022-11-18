import numpy as np
a = np.matrix('1 -2 1; 2 -1 1; 3 2 2') #Варіант 15
print('A=',a)
b = np.matrix('4; 3; 2')
print('B=',b)

c = np.linalg.inv(a)
print(c)
x = c.dot(b)
print('X=',x)