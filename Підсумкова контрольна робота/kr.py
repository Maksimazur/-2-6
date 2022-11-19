import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as intrp

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
time = np.linspace(0, 11, num = 12)
print(time)

plt.plot(time, speed, "b")
plt.xlabel("Час")
plt.ylabel("Швидкість")
plt.grid(True)
plt.show()

xy = intrp.interp1d(time, speed, kind ='cubic')
x2 = np.linspace(0, 11, 10000)
plt.plot(x2, xy(x2), "b")
plt.xlabel("Час")
plt.ylabel("Швидкість")
plt.grid(True)
plt.show()