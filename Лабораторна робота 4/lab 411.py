import numpy as np
a = np.matrix('1 2; 4 -1') #Завдання 1
b = np.matrix('2 -3; -4 1')
c = (a*b)-(b*a)
print(c)