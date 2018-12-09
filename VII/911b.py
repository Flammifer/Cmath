import MyMath as mm
from math import exp, sin, pi
import numpy as np
h = pi/10

flag_eps  =  1
eps_appropriate = 10**(-3)

def func(x):
    return exp(-x**2)*sin(x)
while flag_eps:
    delta = 1.0 #где мы сейчас
    I = 0
    flag = 1
    x = np.array([])
    y = np.array([])
    while flag:
        x = np.append(x, delta)
        y = np.append(y, func(delta))
        delta += h
        I = mm.int_trapeze(x, y)
        if ((exp(-delta)) < (10**(-5))*I):
            flag = 0
    eps = ((delta-1)*(h**2)/6)/I
    print(eps, I)
    if eps < eps_appropriate:
        flag_eps = 0
        print("OK")
    else:
        h = h/2
        print("We have problem with accuracy, current step is:", h)

print(delta, I, exp(-delta))
