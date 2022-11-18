import numpy as np

a = 1.6
b = 2.2
n = 20
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = 1/np.sqrt(pow(x, 2)+0.8)

trapez = round ((h/2)*(f[0] + \
          2 * sum(f[1:n-1]) + f[n-1]), 5)

print("Метод трапецій: ", trapez)