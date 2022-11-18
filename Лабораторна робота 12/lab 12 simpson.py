import numpy as np

a = 0.4
b = 1.2
n = 8
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.cos(pow(x, 2)) / x+1

simp = round ((h/3) * (f[0] + 2*sum(f[:n-2:2]) \
            + 4*sum(f[1:n-1:2]) + f[n-1]), 5)

print("Метод Сімпсона: ", simp)