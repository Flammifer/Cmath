
from math import cos, sin
import numpy as np

def int_linear(c, d, a, b, k): #integrate (cx+b)sin(kx) from a to b
    return c*(a*k*cos(a*k)-sin(a*k)+sin(b*k)-b*k*cos(b*k))/k**2 + d*(cos(a*k)-cos(b*k))/k
def get_linear(x1, y1, x2, y2):
    c = (y2-y1)/(x2-x1)
    d = -c*x1+y1
    return [c, d] # )))
k = 40
x = [0, 1.7, 3.4, 5.1, 6.8]
y = [0, 1.3038, 1.8439, 2.2583 , 2.6077]
I = 0
for i in range(len(x)-1):
    I += int_linear(get_linear(x[i], y[i], x[i+1], y[i+1])[0], get_linear(x[i], y[i], x[i+1], y[i+1])[1], x[i], x[i+1], k)
print(I)
