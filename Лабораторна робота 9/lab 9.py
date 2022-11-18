import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

x = [0.9, 1.2, 1.6, 2.1, 2.8]
y = [3.47, 4.53, 2.86, 1.64, 2.25]

spl = UnivariateSpline(x, y)
xs = np.linspace(0, 2.8, 1000)
plt.title('Spline interpolation')
plt.ylabel('Y')
plt.xlabel('X')
plt.plot(x,y,'ro', xs, spl(xs), 'b')
plt.grid(True)
plt.show()