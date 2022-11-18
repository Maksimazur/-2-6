import numpy as np
from matplotlib import pyplot as plt

x0=1.7
y0=5.3
xp=2.7
n=11
step_h=(xp-x0)/(n-1)

x=np.linspace(x0,xp,n)
y=np.zeros([n])

y[0]=y0
for k in range(1,n):
    y[k]=y[k-1]+step_h*(x[k-1]+np.sin(y[k-1]/np.pi))

for k in range(n):
    print(round(x[k], 5), "\t", round(y[k], 4))

plt.plot(x,y, "o", x,y, "b")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Метод Ейлера")
plt.show()