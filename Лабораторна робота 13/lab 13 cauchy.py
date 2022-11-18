import numpy as np
from matplotlib import pyplot as plt

x0=0.8
y0=1.4
xp=1.8
n=11
step_h=(xp-x0)/(n-1)

x=np.linspace(x0,xp,n)
y=np.zeros([n])

y[0]=y0
for k in range(1,n):
    y[k]=y[k-1]+(step_h/2)*(x[k-1]+np.cos(y[k-1]/np.sqrt(2))+x[k]+np.cos(y[k-1]+step_h*(x[k-1]+np.cos(y[k-1]/np.sqrt(2))/np.sqrt(2))))

for k in range(n):
    print(round(x[k], 5), "\t", round(y[k], 4))

plt.plot(x,y, "o", x,y, "b")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Метод Ейлера-Коші")
plt.show()