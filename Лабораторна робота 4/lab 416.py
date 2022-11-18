import numpy as np
a = np.matrix('1 2 -3; 0 1 2; 0 0 1') #Завдання 1
c = np.linalg.inv(a)
print(c)