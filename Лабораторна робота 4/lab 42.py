import numpy as np
import random

#Завдання 3
n = int(input("Введіть N: "))
m = int(input("Введіть M: "))
a = np.empty((0, m), int)

for i in range (n):
    i = np.empty((0,m), int)
    for t in range (m):
       t = random.randint(1, 100)
       i = np.append(i, t)
    a = np.vstack([a, i])

print(a)

x = np.mean(a, axis=0)
y = np.mean(a, axis=1)
print("Середні значення всіх рядків: ", y)
print("Середні значення всіх стовпців: ", x)