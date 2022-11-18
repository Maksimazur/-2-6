import numpy as np
a = np.matrix('2 3 4; 1 0 6; 7 8 9') #Завдання 1
c = np.linalg.det(a)
print(format(c, '.9g'))