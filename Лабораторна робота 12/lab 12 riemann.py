import numpy as np

a = 0.8
b = 1.8
n = 10
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = 1/np.sqrt(x+4)

rieleft = round (h * sum(f[:n-1]), 5)
rieright = round (h * sum(f[1::]), 5)
riemid = round (h * sum(np.sin((x[:n-1] \
        + x[1:])/2)), 5)

print("Метод лівих прямокутників: ", rieleft)
print("Метод правих прямокутників: ", rieright)
print("Метод середніх прямокутників: ", riemid)