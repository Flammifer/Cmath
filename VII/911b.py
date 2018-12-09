import MyMath as mm
from math import exp, sin, pi
import numpy as np
h = pi/50
x = np.array([])
y = np.array([])
flag = 1
delta = 1.0 #где мы сейчас
I = 0
def func(x):
    return exp(-x**2)*sin(x)
while flag:
    x = np.append(x, delta)
    y = np.append(y, func(delta))

    delta += h
    I = mm.int_trapeze(x, y)
    if ((exp(-delta)) < (10**(-5))*I):
        flag = 0

print(delta, I, exp(-delta))
#print(I)
