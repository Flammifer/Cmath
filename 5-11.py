import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import interpolate
def lin(x, a, b):
    return a*x+b
def sq(m):
    y = []
    for x in m:
        y.append(x**(0.5))
    return y

t = np.linspace(0, 1, 100000)
y = sq(t)
fig = plt.figure()
ax1 = fig.subplots()
popt_n, pcov_n, = curve_fit(lin, t, y)

#ax1.set_ylabel("Amperage, muA")
plt.plot(t, np.polyval(popt_n, t), 'o')
plt.plot(t, y, '-')
print(popt_n)
plt.grid(True)
plt.show()
