import numpy as np
a = np.matrix('1 2 3 4; -2 1 -4 3; 3 -4 -1 2; 4 3 -2 -1') #Завдання 1
c = np.linalg.det(a)
print(format(c, '.9g'))